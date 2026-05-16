import uuid
from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="institutions"
    )
    name = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True, upload_to="institutions/")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Account(models.Model):
    class AccountType(models.TextChoices):
        CREDIT_CARD = "CREDIT_CARD", "Credit Card"
        SAVINGS = "SAVINGS", "Savings"
        INVESTMENT = "INVESTMENT", "Investment"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="accounts"
    )
    institution = models.ForeignKey(
        Institution,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="accounts",
    )
    account_type = models.CharField(max_length=20, choices=AccountType.choices)
    name = models.CharField(max_length=120)
    balance = models.DecimalField(
        decimal_places=4, max_digits=12, default=Decimal("0")
    )
    date_created = models.DateTimeField(auto_now_add=True)

    # Subtype-specific fields — nullable, enforced in clean() and serializer
    cut_date = models.PositiveSmallIntegerField(null=True, blank=True)
    pay_date = models.PositiveSmallIntegerField(null=True, blank=True)
    credit_limit = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True
    )
    is_payroll = models.BooleanField(null=True, blank=True)
    investment_return = models.DecimalField(
        decimal_places=4, max_digits=12, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()})"

    def clean(self):
        super().clean()
        t = self.account_type
        if t == self.AccountType.CREDIT_CARD:
            if any(v is None for v in (self.cut_date, self.pay_date, self.credit_limit)):
                raise ValidationError(
                    "Credit card accounts require cut_date, pay_date, and credit_limit."
                )
            if self.is_payroll is not None or self.investment_return is not None:
                raise ValidationError(
                    "Credit card accounts must not have is_payroll or investment_return."
                )
        elif t == self.AccountType.SAVINGS:
            if self.is_payroll is None:
                raise ValidationError("Savings accounts require is_payroll.")
            if any(
                v is not None
                for v in (self.cut_date, self.pay_date, self.credit_limit, self.investment_return)
            ):
                raise ValidationError(
                    "Savings accounts must not have credit card or investment fields."
                )
        elif t == self.AccountType.INVESTMENT:
            if self.investment_return is None:
                raise ValidationError("Investment accounts require investment_return.")
            if any(
                v is not None
                for v in (self.cut_date, self.pay_date, self.credit_limit, self.is_payroll)
            ):
                raise ValidationError(
                    "Investment accounts must not have credit card or savings fields."
                )

    class Meta:
        ordering = ["name"]


class Category(models.Model):
    class CategoryType(models.TextChoices):
        INCOME = "INCOME", "Income"
        EXPENSE = "EXPENSE", "Expense"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="categories"
    )
    category_type = models.CharField(max_length=10, choices=CategoryType.choices)
    name = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "category_type", "name"],
                name="unique_category_per_user_type",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"


class MoneyMovement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="%(class)ss"
    )
    amount = models.DecimalField(decimal_places=4, max_digits=12)
    is_paid = models.BooleanField(default=False)
    description = models.TextField(blank=True, default="")
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Income(MoneyMovement):
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="incomes"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="incomes",
        limit_choices_to={"category_type": Category.CategoryType.INCOME},
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Income {self.amount} — {self.account}"


class Expense(MoneyMovement):
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="expenses"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="expenses",
        limit_choices_to={"category_type": Category.CategoryType.EXPENSE},
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Expense {self.amount} — {self.account}"


class Transfer(MoneyMovement):
    account_from = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="transfers_from"
    )
    account_to = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="transfers_to"
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Transfer {self.amount} — {self.account_from} to {self.account_to}"
