from decimal import Decimal

import factory
from django.contrib.auth import get_user_model

from accounts.models import Account, Category, Expense, Income, Institution, Transfer

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@test.com")
    password = factory.PostGenerationMethodCall("set_password", "testpass123")


class InstitutionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Institution

    user = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: f"Bank {n}")


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    user = factory.SubFactory(UserFactory)
    institution = factory.SubFactory(InstitutionFactory)
    account_type = Account.AccountType.SAVINGS
    name = factory.Sequence(lambda n: f"Account {n}")
    balance = Decimal("1000.0000")
    is_payroll = True


class CreditCardAccountFactory(AccountFactory):
    account_type = Account.AccountType.CREDIT_CARD
    is_payroll = None
    cut_date = 15
    pay_date = 25
    credit_limit = Decimal("5000.0000")


class SavingsAccountFactory(AccountFactory):
    account_type = Account.AccountType.SAVINGS
    is_payroll = True


class InvestmentAccountFactory(AccountFactory):
    account_type = Account.AccountType.INVESTMENT
    is_payroll = None
    investment_return = Decimal("0.0800")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    user = factory.SubFactory(UserFactory)
    category_type = Category.CategoryType.INCOME
    name = factory.Sequence(lambda n: f"Category {n}")


class IncomeCategoryFactory(CategoryFactory):
    category_type = Category.CategoryType.INCOME


class ExpenseCategoryFactory(CategoryFactory):
    category_type = Category.CategoryType.EXPENSE


class IncomeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Income

    user = factory.SubFactory(UserFactory)
    account = factory.SubFactory(SavingsAccountFactory)
    category = factory.SubFactory(IncomeCategoryFactory)
    amount = Decimal("500.0000")
    is_paid = True
    description = "Test income"
    date = "2025-01-15"


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense

    user = factory.SubFactory(UserFactory)
    account = factory.SubFactory(SavingsAccountFactory)
    category = factory.SubFactory(ExpenseCategoryFactory)
    amount = Decimal("200.0000")
    is_paid = False
    description = "Test expense"
    date = "2025-01-15"


class TransferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transfer

    user = factory.SubFactory(UserFactory)
    account_from = factory.SubFactory(SavingsAccountFactory)
    account_to = factory.SubFactory(InvestmentAccountFactory)
    amount = Decimal("300.0000")
    is_paid = True
    description = "Test transfer"
    date = "2025-01-15"
