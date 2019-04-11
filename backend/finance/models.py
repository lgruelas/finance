from django.db import models
import uuid

# Create your models here.

class Source(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)

    def __str__(self):
        return "source: {}".format(self.name)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    expected = models.DecimalField(decimal_places=4, max_digits=12)

    def __str__(self):
        return "{}, {}".format(self.name, self.expected)

class BankAccount(models.Model):
    source = models.OneToOneField(
        Source,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    bank = models.CharField(max_length=120)
    balance = models.DecimalField(decimal_places=4, max_digits=12)

    def __str__(self):
        return "{}, {}".format(self.source.name, self.balance)

class CreditCard(models.Model):
    source = models.OneToOneField(
        Source,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    cut = models.IntegerField()
    pay = models.IntegerField()
    bank = models.CharField(max_length=120)
    credit = models.DecimalField(decimal_places=4, max_digits=12)
    used = models.DecimalField(decimal_places=4, max_digits=12)

    def __str__(self):
        return "{}, {}".format(self.source.name, self.used)

class Wallet(models.Model):
    source = models.OneToOneField(
        Source,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    balance = models.DecimalField(decimal_places=4, max_digits=12)

    def __str__(self):
        return "{}, {}".format(self.source.name, self.balance)

class Expenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(decimal_places=4, max_digits=12)
    account = models.ForeignKey(Source, on_delete=models.PROTECT)
    is_payed = models.BooleanField(default=1)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date =  models.DateField()

    def __str__(self):
        return "{}, {}, {}, {}".format(self.date, self.amount, self.category, self.account.name)


class Incomes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(decimal_places=4, max_digits=12)
    account = models.ForeignKey(Source, on_delete=models.PROTECT)
    description = models.TextField()
    date =  models.DateField()

    def __str__(self):
        return "{}, {}, {}".format(self.date, self.amount, self.account.name)

class Transfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(decimal_places=4, max_digits=12)
    account_from = models.ForeignKey(Source, on_delete=models.PROTECT, related_name="account_from")
    account_to = models.ForeignKey(Source, on_delete=models.PROTECT, related_name="account_to")
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return "{}, {} => {}, {}".format(self.date, self.account_from.name, self.account_to.name, self.ammount)