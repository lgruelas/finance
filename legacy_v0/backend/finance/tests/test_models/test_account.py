from uuid import uuid4

from django.core.exceptions import ValidationError
from django.test import TestCase

from ...models import Account, BankAccount


class AccountTest(TestCase):
    """ Test module for Account model """
    account_id = uuid4()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Account.objects.create(
            id=cls.account_id,
            name="account_for_test",
            balance=100
        )

    def test_get_child_fails_when_created_alone(self):
        account_alone = Account.objects.get(id=AccountTest.account_id)
        with self.assertRaises(ValidationError):
            account_alone.get_child()

    def test_get_child_success(self):
        bank_account = BankAccount.objects.create(
            name="bank_account_test",
            balance=100,
            bank="bank_test",
            is_investment=True
        )
        related_account = Account.objects.get(id=bank_account.id)
        self.assertTrue(isinstance(related_account.get_child(), BankAccount))

    def test_str_method(self):
        account = Account.objects.get(id=AccountTest.account_id)
        self.assertEqual(str(account), "account_for_test, $100.00")
