import uuid
from model_utils.managers import InheritanceManager

from django.contrib.contenttypes.models import ContentType
from django.db import models


# class Bank(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=120)
#     image = models.ImageField(upload_to='images/banks/')
#     image_invest = models.ImageField(upload_to='images/invest/')

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    balance = models.DecimalField(decimal_places=4, max_digits=12)
    objects = InheritanceManager()

    def get_child(self):
        return Account.objects.get_subclass(pk=self.pk)

    def __str__(self):
        return "account: {}, balance: {}".format(self.name, self.balance)


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    expected = models.DecimalField(decimal_places=4, max_digits=12)
    must_show = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.expected)

    class Meta:
        verbose_name_plural = "Categories"


class BankAccount(Account):
    bank = models.CharField(max_length=120)
    is_investment = models.BooleanField(default=0)

    def __str__(self):
        return "{}, {}".format(self.name, self.balance)


class CreditCard(Account):
    cut = models.IntegerField()
    pay = models.IntegerField()
    bank = models.CharField(max_length=120)
    credit = models.DecimalField(decimal_places=4, max_digits=12)

    @property
    def used(self):
        return self.credit - self.balance

    def __str__(self):
        return "{}, {}".format(self.name, self.balance)


class Wallet(Account):

    def __str__(self):
        return "{}, {}".format(self.name, self.balance)


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(decimal_places=4, max_digits=12)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="expenses")
    is_payed = models.BooleanField(default=1)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="expenses")
    date = models.DateField()

    def __str__(self):
        return "{}, {}, {}, {}".format(self.description, self.amount, self.category, self.account.name)


class Income(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(decimal_places=4, max_digits=12)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="incomes")
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return "{}, {}, {}".format(self.description, self.amount, self.account.name)


class Transfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(decimal_places=4, max_digits=12)
    account_from = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="transfers_origin")
    account_to = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="transfers_destiny")
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return "{}, {} => {}, {}".format(self.description, self.account_from.name, self.account_to.name, self.amount)
