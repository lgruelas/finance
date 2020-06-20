from datetime import date
from uuid import uuid4

from django.test import TestCase

from ...models import BankAccount, Income


class IncomeTest(TestCase):
    """ Test module for Income model """
    income_id = uuid4()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        bank_account = BankAccount.objects.create(
            name="bank_account_income_test",
            balance=150,
            is_investment=True,
            bank="bank_income_test"
        )
        Income.objects.create(
            id=cls.income_id,
            description="income_test",
            amount=50,
            account=bank_account,
            date=date.today().isoformat()
        )

    def test_str_method(self):
        income = Income.objects.get(id=IncomeTest.income_id)
        self.assertEqual(str(income), "income_test, $50.00, bank_account_income_test")
