from django.contrib import admin

from .models import (Institution, Account, SavingsAccount, Invest, CreditCard,
                     Income, IncomeCategory, Expense, ExpenseCategory, Transfer)


# Register your models here.
admin.site.register(Institution)
admin.site.register(Account)
admin.site.register(SavingsAccount)
admin.site.register(CreditCard)
admin.site.register(Invest)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Transfer)
admin.site.register(IncomeCategory)
admin.site.register(ExpenseCategory)
