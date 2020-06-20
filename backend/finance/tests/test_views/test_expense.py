from datetime import date
from rest_framework.test import APIRequestFactory
from unittest.mock import patch, Mock

from django.test import TestCase

from ...views import ExpenseView
from ...models import Account


class ExpenseViewTest(TestCase):
    """ Test module for Expense view """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.dummy_account = Mock(balance=0, id=1)
        self.dummy_category = Mock(id=1)
        self.expense_data = {
            "amount": 10,
            "account_id": self.dummy_account.id,
            "category_id": self.dummy_category.id,
            "description": "expense_description",
            "is_payed": True,
            "date": date.today().isoformat(),
            "account": self.dummy_account
        }

    @patch('finance.views.get_object_or_404')
    @patch('finance.views.ExpenseSerializer')
    def test_create_when_valid(self, mock_serializer, mock_get_object):
        request = self.factory.post("some_url", data=self.expense_data)
        mock_serializer.return_value.is_valid.return_value = True
        mock_get_object.return_value = self.dummy_account

        response = ExpenseView.as_view({"post": "create"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with()
        mock_get_object.assert_called_once_with(Account, id=str(self.dummy_account.id))
        self.assertEqual(self.dummy_account.balance, -self.expense_data["amount"])
        mock_serializer.return_value.save.assert_called_once_with()
        self.dummy_account.save.assert_called_once_with()
        self.assertEqual(response.status_code, 201)

    @patch('finance.views.get_object_or_404')
    @patch('finance.views.ExpenseSerializer')
    def test_create_when_invalid(self, mock_serializer, mock_get_object):
        request = self.factory.post("some_url", data=self.expense_data)
        mock_serializer.return_value.is_valid.return_value = False
        mock_get_object.return_value = self.dummy_account

        response = ExpenseView.as_view({"post": "create"})(request)

        mock_get_object.assert_not_called()
        mock_serializer.return_value.is_valid.assert_called_once_with()
        mock_serializer.return_value.save.assert_not_called()
        self.dummy_account.save.assert_not_called()
        self.assertEqual(response.status_code, 400)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.ExpenseView.get_serializer')
    @patch('finance.views.ExpenseView.get_object')
    def test_update_when_account_and_balance_changes(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url", data=self.expense_data)
        # New objects to be changed
        old_dummy_account = Mock(balance=0, id=2)
        old_expense = Mock(
            amount=5,
            account=old_dummy_account,
            description="old_expense_description",
            date=date.today().isoformat(),
            account_id=old_dummy_account.id
        )
        # Configuring serializer mock with old values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.expense_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_expense
        mock_get_object.return_value = self.dummy_account
        old_expense._prefetched_objects_cache = True

        response = ExpenseView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mock_update.assert_called_once_with([old_dummy_account, self.dummy_account], ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        self.assertEqual(old_expense._prefetched_objects_cache, {})
        self.assertEqual(response.status_code, 200)
        # Check that new account loses the expense
        self.assertEqual(self.dummy_account.balance, -10)
        # Check that previous account gains the expense
        self.assertEqual(old_dummy_account.balance, 5)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.ExpenseView.get_serializer')
    @patch('finance.views.ExpenseView.get_object')
    def test_update_when_balance_changes(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url", data=self.expense_data)
        # New objects to be changed
        old_expense = Mock(
            amount=5,
            account=self.dummy_account,
            description="old_expense_description",
            date=date.today().isoformat(),
            account_id=self.dummy_account.id
        )
        # Configuring serializer mock with old values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.expense_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_expense
        old_expense._prefetched_objects_cache = True

        response = ExpenseView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mock_update.assert_called_once_with([self.dummy_account], ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        mock_get_object.assert_not_called()
        self.assertEqual(old_expense._prefetched_objects_cache, {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.dummy_account.balance, -5)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.ExpenseView.get_serializer')
    @patch('finance.views.ExpenseView.get_object')
    def test_update_with_same_account_and_balance(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url", data=self.expense_data)
        # New objects to be changed
        old_expense = Mock(
            amount=10,
            account=self.dummy_account,
            description="old_expense_description",
            date=date.today().isoformat(),
            account_id=self.dummy_account.id
        )
        # Configuring serializer mock with old values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.expense_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_expense
        old_expense._prefetched_objects_cache = True

        response = ExpenseView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mock_update.assert_called_once_with([self.dummy_account], ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        mock_get_object.assert_not_called()
        self.assertEqual(old_expense._prefetched_objects_cache, {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.dummy_account.balance, 0)

    @patch('finance.views.Account.objects.bulk_update')
    @patch('finance.views.get_object_or_404')
    @patch('finance.views.ExpenseView.get_serializer')
    @patch('finance.views.ExpenseView.get_object')
    def test_update_when_no_cache(self, mock_instance, mock_serializer, mock_get_object, mock_update):
        request = self.factory.put("some_url", data=self.expense_data)
        # New objects to be changed
        old_expense = Mock(
            amount=10,
            account=self.dummy_account,
            description="old_expense_description",
            date=date.today().isoformat(),
            account_id=self.dummy_account.id
        )
        # Configuring serializer mock with old values
        mock_serializer.return_value.is_valid.return_value = True
        mock_serializer.return_value.validated_data = self.expense_data
        # Configuring instance mock with old values
        mock_instance.return_value = old_expense
        old_expense._prefetched_objects_cache = False

        response = ExpenseView.as_view({"put": "update"})(request)

        mock_serializer.return_value.is_valid.assert_called_once_with(raise_exception=True)
        mock_update.assert_called_once_with([self.dummy_account], ["balance"])
        mock_serializer.return_value.save.assert_called_once_with()
        mock_get_object.assert_not_called()
        self.assertFalse(getattr(old_expense, '_prefetched_objects_cache', True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.dummy_account.balance, 0)

    @patch('finance.views.ExpenseView.get_object')
    def test_destroy(self, mock_instance):
        request = self.factory.delete("some_url")
        expense = Mock(**self.expense_data)
        mock_instance.return_value = expense

        response = ExpenseView.as_view({"delete": "destroy"})(request)

        self.dummy_account.save.assert_called_once_with()
        expense.delete.assert_called_once_with()
        self.assertEqual(self.dummy_account.balance, 10)
        self.assertEqual(response.status_code, 204)
