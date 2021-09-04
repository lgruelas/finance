from datetime import date
from uuid import uuid4

from django.test import TestCase

from ...models import BankAccount, Transfer


class TransferTest(TestCase):
    """ Test module for Transfer model """
    transfer_id = uuid4()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        account_from = BankAccount.objects.create(
            name="transfer_from",
            balance=150,
            is_investment=True,
            bank="bank_transfer_test"
        )
        account_to = BankAccount.objects.create(
            name="transfer_to",
            balance=150,
            is_investment=True,
            bank="bank_transfer_test"
        )
        Transfer.objects.create(
            id=cls.transfer_id,
            description="transfer_test",
            amount=150,
            account_from=account_from,
            account_to=account_to,
            date=date.today().isoformat()
        )

    def test_str_method(self):
        transfer = Transfer.objects.get(id=TransferTest.transfer_id)
        expected_str = "transfer_test, transfer_from => transfer_to, $150.00"
        self.assertEqual(str(transfer), expected_str)
