from uuid import uuid4

from django.test import TestCase

from ...models import CreditCard


class CreditCardTest(TestCase):
    """ Test module for CreditCard model """
    credit_card_id = uuid4()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        CreditCard.objects.create(
            id=cls.credit_card_id,
            name="credit_card_test",
            balance=150,
            bank="bank_test",
            cut=5,
            pay=20,
            credit=5000
        )

    def test_str_method(self):
        credit_card = CreditCard.objects.get(id=CreditCardTest.credit_card_id)
        self.assertEqual(str(credit_card), "credit_card_test, $150.00")

    def test_used(self):
        credit_card = CreditCard.objects.get(id=CreditCardTest.credit_card_id)
        self.assertEqual(credit_card.used, 5000 - 150)
