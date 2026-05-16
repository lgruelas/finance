from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError

from accounts.factories import (
    AccountFactory,
    CreditCardAccountFactory,
    InvestmentAccountFactory,
    SavingsAccountFactory,
    UserFactory,
)
from accounts.models import Account, Category


@pytest.mark.django_db
class TestAccountValidation:
    def test_credit_card_requires_subtype_fields(self):
        account = Account(
            account_type=Account.AccountType.CREDIT_CARD,
            name="Test Card",
            balance=Decimal("0"),
        )
        with pytest.raises(ValidationError, match="Credit card accounts require"):
            account.clean()

    def test_credit_card_valid_with_all_fields(self):
        account = CreditCardAccountFactory()
        account.clean()  # should not raise

    def test_credit_card_rejects_savings_fields(self):
        account = Account(
            account_type=Account.AccountType.CREDIT_CARD,
            name="Test Card",
            balance=Decimal("0"),
            cut_date=15,
            pay_date=25,
            credit_limit=Decimal("5000"),
            is_payroll=True,
        )
        with pytest.raises(ValidationError, match="must not have is_payroll"):
            account.clean()

    def test_savings_requires_is_payroll(self):
        account = Account(
            account_type=Account.AccountType.SAVINGS,
            name="Test Savings",
            balance=Decimal("0"),
        )
        with pytest.raises(ValidationError, match="Savings accounts require is_payroll"):
            account.clean()

    def test_savings_valid_with_is_payroll(self):
        account = SavingsAccountFactory()
        account.clean()  # should not raise

    def test_savings_rejects_credit_card_fields(self):
        account = Account(
            account_type=Account.AccountType.SAVINGS,
            name="Test Savings",
            balance=Decimal("0"),
            is_payroll=False,
            credit_limit=Decimal("1000"),
        )
        with pytest.raises(ValidationError, match="must not have credit card"):
            account.clean()

    def test_investment_requires_investment_return(self):
        account = Account(
            account_type=Account.AccountType.INVESTMENT,
            name="Test Investment",
            balance=Decimal("0"),
        )
        with pytest.raises(ValidationError, match="Investment accounts require"):
            account.clean()

    def test_investment_valid_with_return(self):
        account = InvestmentAccountFactory()
        account.clean()  # should not raise


@pytest.mark.django_db
class TestCategoryConstraint:
    def test_unique_category_per_user_type(self):
        user = UserFactory()
        Category.objects.create(user=user, category_type=Category.CategoryType.INCOME, name="Salary")
        with pytest.raises(Exception):
            Category.objects.create(user=user, category_type=Category.CategoryType.INCOME, name="Salary")

    def test_same_name_different_type_is_ok(self):
        user = UserFactory()
        Category.objects.create(user=user, category_type=Category.CategoryType.INCOME, name="Other")
        Category.objects.create(user=user, category_type=Category.CategoryType.EXPENSE, name="Other")

    def test_same_name_different_user_is_ok(self):
        user = UserFactory()
        another = UserFactory()
        Category.objects.create(user=user, category_type=Category.CategoryType.INCOME, name="Salary")
        Category.objects.create(user=another, category_type=Category.CategoryType.INCOME, name="Salary")


class TestStrMethods:
    def test_account_str(self):
        account = AccountFactory.build(name="Chase Sapphire", account_type=Account.AccountType.CREDIT_CARD)
        assert "Chase Sapphire" in str(account)
        assert "Credit Card" in str(account)

    def test_category_str(self):
        cat = Category(category_type=Category.CategoryType.INCOME, name="Salary")
        assert "Salary" in str(cat)
        assert "Income" in str(cat)
