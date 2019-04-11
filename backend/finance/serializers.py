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