from datetime import date
from rest_framework.test import APIRequestFactory
from unittest.mock import patch, Mock

from django.test import TestCase

from ...views import TransferView
from ...models import Account, CreditCard


class TransferViewTest(TestCase):
    """ Test module for Transfer view """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.dummy_account_from = Mock(id=1, balance=0)
        self.dummy_account_to = Mock(id=2, balance=0)
        self.transfer_data = {
            "amount": 10,
            "description": "transfer_test",
            "date": date.today().isoformat(),
            # For seralizer
            "account_from_id": self.dummy_account_from.id,
            "account_to_id": self.dummy_account_to.id,
            # For instance
            "account_from": self.dummy_account_from,
            "account_to": self.dummy_account_to
        }

    @patch('finance.views.get_object_or_404')
    @patch('finance.views.TransferSerializer')
    def test_create_when_valid(self, mock_serializer, mock_get_object):
        request = self.factory.post("some_url", data=self.transfer_data)
        mock_serializer.return_value.is_valid.return_value = True
        mock_get_object.side_effect = [self.dummy_account_from, self.dummy_account_to]

        response = TransferView.as_view({"post": "create"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with()
        self.assertEqual(mock_get_object.call_count, 2)
        self.assertEqual(self.dummy_account_from.balance, -self.transfer_data["amount"])
        self.assertEqual(self.dummy_account_to.balance, self.transfer_data["amount"])
        mock_serializer.return_value.save.assert_called_once_with()
        self.dummy_account_from.save.assert_called_once_with()
        self.dummy_account_to.save.assert_called_once_with()
        self.assertEqual(response.status_code, 201)

    @patch('finance.views.get_object_or_404')
    @patch('finance.views.TransferSerializer')
    def test_create_raises_exception_when_credit_card(self, mock_serializer, mock_get_object):
        request = self.factory.post("some_url", data=self.transfer_data)
        card_mock = Mock(spec=CreditCard)
        mock_serializer.return_value.is_valid.return_value = True
        mock_get_object.side_effect = [card_mock, self.dummy_account_to]

        response = TransferView.as_view({"post": "create"})(request)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(mock_get_object.call_count, 2)
        mock_serializer.return_value.is_valid.assert_called_once_with()
        mock_serializer.return_value.save.assert_not_called()
        card_mock.save.assert_not_called()
        self.dummy_account_to.save.assert_not_called()

    @patch('finance.views.get_object_or_404')
    @patch('finance.views.TransferSerializer')
    def test_create_when_invalid(self, mock_serializer, mock_get_object):
        request = self.factory.post("some_url", data=self.transfer_data)
        mock_serializer.return_value.is_valid.return_value = False

        response = TransferView.as_view({"post": "create"})(request)

        mock_get_object.assert_not_called()
        mock_serializer.return_value.is_valid.assert_called_once_with()
        mock_serializer.return_value.save.assert_not_called()
        self.dummy_account_from.save.assert_not_called()
        self.dummy_account_to.save.assert_not_called()
        self.assertEqual(response.status_code, 400)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.TransferView.get_serializer')
    @patch('finance.views.TransferView.get_object')
    def test_update(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url", data=self.transfer_data)
        # Old objects to be changed
        old_dummy_account_from = Mock(balance=0, id=3)
        old_dummy_account_to = Mock(balance=0, id=4)
        old_transfer = Mock(
            amount=5,
            account_from=old_dummy_account_from,
            account_to=old_dummy_account_to,
            description="new_transfer_description",
            date=date.today().isoformat()
        )
        # Configuring serializer mock with new values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.transfer_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_transfer
        mock_get_object.side_effect = [self.dummy_account_from, self.dummy_account_to]
        old_transfer._prefetched_objects_cache = True

        response = TransferView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mod_accounts = [old_dummy_account_from, old_dummy_account_to, self.dummy_account_from, self.dummy_account_to]
        mock_update.assert_called_once_with(mod_accounts, ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        self.assertEqual(old_transfer._prefetched_objects_cache, {})
        self.assertEqual(response.status_code, 200)
        # Check that old accounts loses the transfer
        self.assertEqual(old_dummy_account_from.balance, 5)
        self.assertEqual(old_dummy_account_to.balance, -5)
        # Check that new accounts gains the transfer
        self.assertEqual(self.dummy_account_from.balance, -10)
        self.assertEqual(self.dummy_account_to.balance, 10)

    @patch('finance.views.TransferView.get_object')
    def test_destroy(self, mock_instance):
        request = self.factory.delete("some_url")
        transfer = Mock(**self.transfer_data)
        mock_instance.return_value = transfer

        response = TransferView.as_view({"delete": "destroy"})(request)

        self.dummy_account_from.save.assert_called_once_with()
        self.dummy_account_to.save.assert_called_once_with()
        transfer.delete.assert_called_once_with()
        self.assertEqual(self.dummy_account_from.balance, 10)
        self.assertEqual(self.dummy_account_to.balance, -10)
        self.assertEqual(response.status_code, 204)
