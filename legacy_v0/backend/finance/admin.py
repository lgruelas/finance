from django.contrib import admin
from .models import Wallet, BankAccount, CreditCard, Category, Expense,\
    Income, Transfer, Account

# Register your models here.
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(BankAccount)
admin.site.register(CreditCard)
admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Transfer)
