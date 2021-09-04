from uuid import uuid4

from django.test import TestCase

from ...models import BankAccount


class BankAccountTest(TestCase):
    """ Test module for BankAccount model """
    bank_account_id = uuid4()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        BankAccount.objects.create(
            id=cls.bank_account_id,
            name="bank_account_test",
            balance=150,
            is_investment=True,
            bank="bank_test"
        )

    def test_str_method(self):
        bank_account = BankAccount.objects.get(id=BankAccountTest.bank_account_id)
        self.assertEqual(str(bank_account), "bank_account_test, $150.00")
