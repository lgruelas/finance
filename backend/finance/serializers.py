from rest_framework import serializers
from .models import Wallet, BankAccount, CreditCard, Category, Expense, Income, Transfer

class WalletSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('__all__')


class BankAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('__all__')


class CreditCardSerializers(serializers.ModelSerializer):

    class Meta:
        model = CreditCard
        fields = ('__all__')


class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('__all__')


class IncomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('__all__')


class TransferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class CategoryByMonthSerializers(serializers.ModelSerializer):

    def used_amount(self, category):
        my_expenses = self.context.get('expenses').filter(category=category.id)
        return sum([i.amount for i in my_expenses])

    class Meta:
        model = Category
        fields = ('id', 'name', 'expected', 'used', 'must_show')
