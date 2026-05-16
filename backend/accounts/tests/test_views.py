from decimal import Decimal

import pytest
from django.contrib.auth import get_user_model

from accounts.factories import (
    CreditCardAccountFactory,
    ExpenseCategoryFactory,
    IncomeCategoryFactory,
    InstitutionFactory,
    InvestmentAccountFactory,
    SavingsAccountFactory,
    UserFactory,
)
from accounts.models import Account, Category, Expense, Income, Institution, Transfer

User = get_user_model()

INSTITUTION_URL = "/api/v1/institutions/"
ACCOUNT_URL = "/api/v1/accounts/"
CATEGORY_URL = "/api/v1/categories/"
INCOME_URL = "/api/v1/incomes/"
EXPENSE_URL = "/api/v1/expenses/"
TRANSFER_URL = "/api/v1/transfers/"


class TestAuthRequired:
    @pytest.mark.parametrize(
        "url",
        [INSTITUTION_URL, ACCOUNT_URL, CATEGORY_URL, INCOME_URL, EXPENSE_URL, TRANSFER_URL],
    )
    def test_unauthenticated_get_returns_401(self, api_client, url):
        response = api_client.get(url)
        assert response.status_code == 401


@pytest.mark.django_db
class TestInstitutionViews:
    def test_list_own_institutions(self, auth_client):
        client, user = auth_client
        InstitutionFactory(user=user, name="My Bank")
        InstitutionFactory(name="Other Bank")
        response = client.get(INSTITUTION_URL)
        assert response.status_code == 200
        assert response.data["count"] == 1
        assert response.data["results"][0]["name"] == "My Bank"

    def test_create_institution(self, auth_client):
        client, user = auth_client
        response = client.post(INSTITUTION_URL, {"name": "New Bank"}, format="json")
        assert response.status_code == 201
        assert Institution.objects.filter(user=user, name="New Bank").exists()

    def test_cannot_see_other_users_institution(self, auth_client_for_user):
        other = UserFactory()
        inst = InstitutionFactory(user=other)
        client = auth_client_for_user(UserFactory())
        response = client.get(f"{INSTITUTION_URL}{inst.id}/")
        assert response.status_code == 404


@pytest.mark.django_db
class TestAccountViews:
    def test_create_savings_account(self, auth_client):
        client, user = auth_client
        inst = InstitutionFactory(user=user)
        data = {
            "account_type": Account.AccountType.SAVINGS,
            "name": "My Savings",
            "balance": "1000",
            "is_payroll": True,
            "institution": inst.id,
        }
        response = client.post(ACCOUNT_URL, data, format="json")
        assert response.status_code == 201
        assert Account.objects.filter(user=user, name="My Savings").exists()

    def test_create_credit_card_account(self, auth_client):
        client, user = auth_client
        data = {
            "account_type": Account.AccountType.CREDIT_CARD,
            "name": "My Card",
            "balance": "0",
            "cut_date": 15,
            "pay_date": 25,
            "credit_limit": "5000",
        }
        response = client.post(ACCOUNT_URL, data, format="json")
        assert response.status_code == 201

    def test_filter_by_account_type(self, auth_client):
        client, user = auth_client
        SavingsAccountFactory(user=user)
        CreditCardAccountFactory(user=user)
        response = client.get(ACCOUNT_URL, {"account_type": Account.AccountType.SAVINGS})
        assert response.status_code == 200
        assert response.data["count"] == 1

    def test_invalid_account_type_returns_400(self, auth_client):
        client, user = auth_client
        data = {"account_type": "INVALID", "name": "Bad", "balance": "0"}
        response = client.post(ACCOUNT_URL, data, format="json")
        assert response.status_code == 400


@pytest.mark.django_db
class TestCategoryViews:
    def test_create_category(self, auth_client):
        client, user = auth_client
        data = {"category_type": Category.CategoryType.INCOME, "name": "Salary"}
        response = client.post(CATEGORY_URL, data, format="json")
        assert response.status_code == 201

    def test_filter_by_category_type(self, auth_client):
        client, user = auth_client
        IncomeCategoryFactory(user=user)
        ExpenseCategoryFactory(user=user)
        response = client.get(CATEGORY_URL, {"category_type": Category.CategoryType.INCOME})
        assert response.status_code == 200
        assert response.data["count"] == 1


@pytest.mark.django_db
class TestIncomeViews:
    def test_create_income(self, auth_client):
        client, user = auth_client
        account = SavingsAccountFactory(user=user)
        category = IncomeCategoryFactory(user=user)
        data = {
            "account": account.id,
            "category": category.id,
            "amount": "500",
            "date": "2025-01-15",
        }
        response = client.post(INCOME_URL, data, format="json")
        assert response.status_code == 201
        assert Income.objects.filter(user=user).exists()

    def test_cannot_use_other_users_account(self, auth_client, another_user):
        client, user = auth_client
        account = SavingsAccountFactory(user=another_user)
        category = IncomeCategoryFactory(user=user)
        data = {
            "account": account.id,
            "category": category.id,
            "amount": "500",
            "date": "2025-01-15",
        }
        response = client.post(INCOME_URL, data, format="json")
        assert response.status_code == 400


@pytest.mark.django_db
class TestExpenseViews:
    def test_create_expense(self, auth_client):
        client, user = auth_client
        account = SavingsAccountFactory(user=user)
        category = ExpenseCategoryFactory(user=user)
        data = {
            "account": account.id,
            "category": category.id,
            "amount": "200",
            "date": "2025-01-15",
        }
        response = client.post(EXPENSE_URL, data, format="json")
        assert response.status_code == 201


@pytest.mark.django_db
class TestTransferViews:
    def test_create_transfer(self, auth_client):
        client, user = auth_client
        account_from = SavingsAccountFactory(user=user)
        account_to = InvestmentAccountFactory(user=user)
        data = {
            "account_from": account_from.id,
            "account_to": account_to.id,
            "amount": "300",
            "date": "2025-01-15",
        }
        response = client.post(TRANSFER_URL, data, format="json")
        assert response.status_code == 201
        assert Transfer.objects.filter(user=user).exists()

    def test_same_account_transfer_rejected(self, auth_client):
        client, user = auth_client
        account = SavingsAccountFactory(user=user)
        data = {
            "account_from": account.id,
            "account_to": account.id,
            "amount": "100",
            "date": "2025-01-15",
        }
        response = client.post(TRANSFER_URL, data, format="json")
        assert response.status_code == 400


@pytest.mark.django_db
class TestPagination:
    def test_paginated_response(self, auth_client):
        client, user = auth_client
        for _ in range(3):
            InstitutionFactory(user=user)
        response = client.get(INSTITUTION_URL)
        assert response.status_code == 200
        assert "count" in response.data
        assert "results" in response.data
