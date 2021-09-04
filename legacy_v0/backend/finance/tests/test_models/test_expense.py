from datetime import date
from uuid import uuid4

from django.test import TestCase

from ...models import BankAccount, Category, Expense


class ExpenseTest(TestCase):
    """ Test module for Expense model """
    expense_id = uuid4()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        bank_account = BankAccount.objects.create(
            name="bank_account_expense_test",
            balance=150,
            is_investment=True,
            bank="bank_expense_test"
        )
        category = Category.objects.create(
            name="category_expense_test",
            must_show=True,
            expected=3000,
            is_active=True
        )
        Expense.objects.create(
            id=cls.expense_id,
            description="expense_test",
            amount=50,
            is_payed=True,
            category=category,
            account=bank_account,
            date=date.today().isoformat()
        )

    def test_str_method(self):
        expense = Expense.objects.get(id=ExpenseTest.expense_id)
        self.assertEqual(str(expense), "expense_test, $50.00, category_expense_test, bank_account_expense_test")
