from datetime import date
from rest_framework.test import APIRequestFactory
from unittest.mock import patch, Mock

from django.test import TestCase

from ...views import IncomeView
from ...models import Account


class IncomeViewTest(TestCase):
    """ Test module for Income view """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.dummy_account = Mock(balance=0, id=1)
        self.income_data = {
            "amount": 10,
            "account_id": self.dummy_account.id,
            "description": "income_description",
            "date": date.today().isoformat()
        }

    @patch('finance.views.get_object_or_404')
    @patch('finance.views.IncomeSerializer')
    def test_create_when_valid(self, mock_serializer, mock_get_object):
        request = self.factory.post("some_url", data=self.income_data)
        mock_serializer.return_value.is_valid.return_value = True
        mock_get_object.return_value = self.dummy_account

        response = IncomeView.as_view({"post": "create"})(request)

        mock_get_object.assert_called_once_with(Account, id=str(self.dummy_account.id))
        mock_serializer.return_value.is_valid.assert_called_once_with()
        mock_serializer.return_value.save.assert_called_once_with()
        self.dummy_account.save.assert_called_once_with()
        self.assertEqual(self.dummy_account.balance, self.income_data["amount"])
        self.assertEqual(response.status_code, 201)

    @patch('finance.views.get_object_or_404')
    @patch('finance.views.IncomeSerializer')
    def test_create_when_invalid(self, mock_serializer, mock_get_object):
        request = self.factory.post("some_url", data=self.income_data)
        mock_serializer.return_value.is_valid.return_value = False
        mock_get_object.return_value = self.dummy_account

        response = IncomeView.as_view({"post": "create"})(request)

        mock_get_object.assert_not_called()
        mock_serializer.return_value.is_valid.assert_called_once_with()
        mock_serializer.return_value.save.assert_not_called()
        self.dummy_account.save.assert_not_called()
        self.assertEqual(response.status_code, 400)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.IncomeView.get_serializer')
    @patch('finance.views.IncomeView.get_object')
    def test_update_when_balance_and_account_change(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url", data=self.income_data)
        # Old objects to be changed
        old_dummy_account = Mock(balance=0, id=2)
        old_income = Mock(
            amount=5,
            account=old_dummy_account,
            description="new_income_description",
            date=date.today().isoformat()
        )
        # Configuring serializer mock with new values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.income_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_income
        mock_get_object.return_value = self.dummy_account
        old_income._prefetched_objects_cache = True

        response = IncomeView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mock_update.assert_called_once_with([old_dummy_account, self.dummy_account], ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        self.assertEqual(old_income._prefetched_objects_cache, {})
        self.assertEqual(response.status_code, 200)
        # Check that new account gains the income
        self.assertEqual(self.dummy_account.balance, 10)
        # Check that previous account losses the income
        self.assertEqual(old_dummy_account.balance, -5)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.IncomeView.get_serializer')
    @patch('finance.views.IncomeView.get_object')
    def test_update_when_balance_changes(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url", data=self.income_data)
        # New objects to be changed
        old_income = Mock(
            amount=5,
            account=self.dummy_account,
            description="old_income_description",
            date=date.today().isoformat(),
            account_id=self.dummy_account.id
        )
        # Configuring serializer mock with old values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.income_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_income
        old_income._prefetched_objects_cache = True

        response = IncomeView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mock_update.assert_called_once_with([self.dummy_account], ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        mock_get_object.assert_not_called()
        self.assertEqual(old_income._prefetched_objects_cache, {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.dummy_account.balance, 5)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.IncomeView.get_serializer')
    @patch('finance.views.IncomeView.get_object')
    def test_update_with_same_account_and_balance(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url this string is intended to bee too long so flake8 will fail", data=self.income_data)
        # New objects to be changed
        old_income = Mock(
            amount=10,
            account=self.dummy_account,
            description="old_income_description",
            date=date.today().isoformat(),
            account_id=self.dummy_account.id
        )
        # Configuring serializer mock with old values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.income_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_income
        old_income._prefetched_objects_cache = True

        response = IncomeView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mock_update.assert_called_once_with([self.dummy_account], ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        mock_get_object.assert_not_called()
        self.assertEqual(old_income._prefetched_objects_cache, {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.dummy_account.balance, 0)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.IncomeView.get_serializer')
    @patch('finance.views.IncomeView.get_object')
    def test_update_when_no_cache(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url", data=self.income_data)
        # New objects to be changed
        old_income = Mock(
            amount=10,
            account=self.dummy_account,
            description="old_income_description",
            date=date.today().isoformat(),
            account_id=self.dummy_account.id
        )
        # Configuring serializer mock with old values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.income_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_income
        old_income._prefetched_objects_cache = False

        response = IncomeView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mock_update.assert_called_once_with([self.dummy_account], ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        mock_get_object.assert_not_called()
        self.assertFalse(getattr(old_income, '_prefetched_objects_cache', True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.dummy_account.balance, 0)

    @patch('finance.views.IncomeView.get_object')
    def test_destroy(self, mock_instance):
        request = self.factory.delete("some_url")
        income = Mock(
            amount=10,
            account=self.dummy_account,
            description="new_income_description",
            date=date.today().isoformat()
        )
        mock_instance.return_value = income

        response = IncomeView.as_view({"delete": "destroy"})(request)

        self.dummy_account.save.assert_called_once_with()
        income.delete.assert_called_once_with()
        self.assertEqual(self.dummy_account.balance, -10)
        self.assertEqual(response.status_code, 204)
