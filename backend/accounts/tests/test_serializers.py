from decimal import Decimal

import pytest
from rest_framework.test import APIRequestFactory

from accounts.factories import (
    AccountFactory,
    CategoryFactory,
    ExpenseCategoryFactory,
    IncomeCategoryFactory,
    IncomeFactory,
    SavingsAccountFactory,
    UserFactory,
)
from accounts.models import Account, Category
from accounts.serializers import (
    AccountSerializer,
    CategorySerializer,
    ExpenseSerializer,
    IncomeSerializer,
    TransferSerializer,
)

factory = APIRequestFactory()


def _make_request(user):
    request = factory.get("/")
    request.user = user
    return request


@pytest.mark.django_db
class TestAccountSerializer:
    def test_valid_credit_card(self):
        user = UserFactory()
        data = {
            "account_type": Account.AccountType.CREDIT_CARD,
            "name": "My Card",
            "balance": "0",
            "cut_date": 15,
            "pay_date": 25,
            "credit_limit": "5000",
        }
        serializer = AccountSerializer(data=data, context={"request": _make_request(user)})
        assert serializer.is_valid(), serializer.errors

    def test_credit_card_missing_required_fields(self):
        user = UserFactory()
        data = {
            "account_type": Account.AccountType.CREDIT_CARD,
            "name": "My Card",
            "balance": "0",
        }
        serializer = AccountSerializer(data=data, context={"request": _make_request(user)})
        assert not serializer.is_valid()
        assert "cut_date" in serializer.errors
        assert "pay_date" in serializer.errors
        assert "credit_limit" in serializer.errors

    def test_credit_card_with_forbidden_fields(self):
        user = UserFactory()
        data = {
            "account_type": Account.AccountType.CREDIT_CARD,
            "name": "My Card",
            "balance": "0",
            "cut_date": 15,
            "pay_date": 25,
            "credit_limit": "5000",
            "is_payroll": True,
        }
        serializer = AccountSerializer(data=data, context={"request": _make_request(user)})
        assert not serializer.is_valid()
        assert "is_payroll" in serializer.errors

    def test_valid_savings(self):
        user = UserFactory()
        data = {
            "account_type": Account.AccountType.SAVINGS,
            "name": "My Savings",
            "balance": "1000",
            "is_payroll": True,
        }
        serializer = AccountSerializer(data=data, context={"request": _make_request(user)})
        assert serializer.is_valid(), serializer.errors

    def test_valid_investment(self):
        user = UserFactory()
        data = {
            "account_type": Account.AccountType.INVESTMENT,
            "name": "My Invest",
            "balance": "5000",
            "investment_return": "0.08",
        }
        serializer = AccountSerializer(data=data, context={"request": _make_request(user)})
        assert serializer.is_valid(), serializer.errors

    def test_partial_update_ignores_missing_required(self):
        user = UserFactory()
        account = AccountFactory(user=user, account_type=Account.AccountType.SAVINGS, is_payroll=True)
        data = {"balance": "2000"}
        serializer = AccountSerializer(account, data=data, partial=True, context={"request": _make_request(user)})
        assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
class TestCategorySerializer:
    def test_valid_category(self):
        user = UserFactory()
        data = {"category_type": Category.CategoryType.INCOME, "name": "Salary"}
        serializer = CategorySerializer(data=data, context={"request": _make_request(user)})
        assert serializer.is_valid(), serializer.errors

    def test_cannot_change_type_with_transactions(self):
        user = UserFactory()
        cat = IncomeCategoryFactory(user=user)
        IncomeFactory(user=user, category=cat, account=SavingsAccountFactory(user=user))
        data = {"category_type": Category.CategoryType.EXPENSE}
        serializer = CategorySerializer(cat, data=data, partial=True, context={"request": _make_request(user)})
        assert not serializer.is_valid()
        assert "category_type" in serializer.errors


@pytest.mark.django_db
class TestIncomeSerializer:
    def test_rejects_expense_category(self):
        user = UserFactory()
        account = SavingsAccountFactory(user=user)
        category = ExpenseCategoryFactory(user=user)
        data = {
            "account": account.id,
            "category": category.id,
            "amount": "500",
            "date": "2025-01-15",
        }
        serializer = IncomeSerializer(data=data, context={"request": _make_request(user)})
        assert not serializer.is_valid()
        assert "category" in serializer.errors

    def test_rejects_other_users_account(self):
        user = UserFactory()
        other = UserFactory()
        account = SavingsAccountFactory(user=other)
        category = IncomeCategoryFactory(user=user)
        data = {
            "account": account.id,
            "category": category.id,
            "amount": "500",
            "date": "2025-01-15",
        }
        serializer = IncomeSerializer(data=data, context={"request": _make_request(user)})
        assert not serializer.is_valid()
        assert "account" in serializer.errors


@pytest.mark.django_db
class TestExpenseSerializer:
    def test_rejects_income_category(self):
        user = UserFactory()
        account = SavingsAccountFactory(user=user)
        category = IncomeCategoryFactory(user=user)
        data = {
            "account": account.id,
            "category": category.id,
            "amount": "200",
            "date": "2025-01-15",
        }
        serializer = ExpenseSerializer(data=data, context={"request": _make_request(user)})
        assert not serializer.is_valid()
        assert "category" in serializer.errors


@pytest.mark.django_db
class TestTransferSerializer:
    def test_rejects_same_account(self):
        user = UserFactory()
        account = SavingsAccountFactory(user=user)
        data = {
            "account_from": account.id,
            "account_to": account.id,
            "amount": "100",
            "date": "2025-01-15",
        }
        serializer = TransferSerializer(data=data, context={"request": _make_request(user)})
        assert not serializer.is_valid()
        assert "Source and destination" in str(serializer.errors)

    def test_rejects_other_users_account(self):
        user = UserFactory()
        other = UserFactory()
        account_from = SavingsAccountFactory(user=user)
        account_to = SavingsAccountFactory(user=other)
        data = {
            "account_from": account_from.id,
            "account_to": account_to.id,
            "amount": "100",
            "date": "2025-01-15",
        }
        serializer = TransferSerializer(data=data, context={"request": _make_request(user)})
        assert not serializer.is_valid()
        assert "account_to" in serializer.errors
