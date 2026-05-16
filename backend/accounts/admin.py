from django.contrib import admin

from .models import Account, Category, Expense, Income, Institution, Transfer, User


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["name", "account_type", "balance", "institution", "user", "date_created"]
    list_filter = ["account_type", "user"]
    search_fields = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category_type", "user", "date_created"]
    list_filter = ["category_type", "user"]
    search_fields = ["name"]


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["account", "category", "amount", "is_paid", "date"]
    list_filter = ["is_paid", "date"]


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["account", "category", "amount", "is_paid", "date"]
    list_filter = ["is_paid", "date"]


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ["account_from", "account_to", "amount", "is_paid", "date"]
    list_filter = ["is_paid", "date"]


admin.site.register(User)
admin.site.register(Institution)
