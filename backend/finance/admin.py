from django.contrib import admin
from .models import Wallet, Source, BankAccount, CreditCard, Category, Expenses, Incomes, Transfer

# Register your models here.
admin.site.register(Wallet)
admin.site.register(Source)
admin.site.register(BankAccount)
admin.site.register(CreditCard)
admin.site.register(Category)
admin.site.register(Expenses)
admin.site.register(Incomes)
admin.site.register(Transfer)
