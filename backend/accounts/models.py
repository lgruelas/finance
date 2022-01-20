import uuid

from django.db import models


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(decimal_places=4, max_digits=12)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=120, default="")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.institution.name}-{self.name}"


class CreditCard(Account):
    cut_date = models.IntegerField()
    pay_date = models.IntegerField()
    credit_limit = models.DecimalField(decimal_places=4, max_digits=12)


class SavingsAccount(Account):
    is_payroll = models.BooleanField(default=False)


class Invest(Account):
    investment_return = models.DecimalField(decimal_places=4, max_digits=12)


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class IncomeCategory(Category):
    class Meta:
        verbose_name_plural = "Income Categories"


class ExpenseCategory(Category):
    class Meta:
        verbose_name_plural = "Expense Categories"


class MoneyMovement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(decimal_places=4, max_digits=12)
    is_payed = models.BooleanField(default=True)
    description = models.TextField()
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Income(MoneyMovement):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="incomes", null=True)
    income_category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, related_name="incomes", null=True)


class Expense(MoneyMovement):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="expenses", null=True)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, related_name="expenses", null=True)


class Transfer(MoneyMovement):
    account_from = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="transfers_origin", null=True)
    account_to = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="transfers_destiny", null=True)
