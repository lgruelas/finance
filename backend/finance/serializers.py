from rest_framework import serializers
from .models import Wallet, Source, BankAccount, CreditCard, Category, Expenses, Incomes, Transfer

class SourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name')

class WalletSerializers(serializers.ModelSerializer):
    source = SourceSerializers(read_only=True)
    class Meta:
        model = Wallet
        fields = ('balance', 'source')

class BankAccountSerializers(serializers.ModelSerializer):
    source = SourceSerializers(read_only=True)
    class Meta:
        model = BankAccount
        fields = ('balance', 'source', 'bank'),

class CreditCardSerializers(serializers.ModelSerializer):
    source = SourceSerializers(read_only=True)
    class Meta:
        model = CreditCard
        fields = ('__all__')

class ExpensesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ('__all__')

class IncomesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Incomes
        fields = ('__all__')

class TransferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')