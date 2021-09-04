from rest_framework import serializers
from .models import Account, Wallet, BankAccount, CreditCard, Category, Expense, Income, Transfer


class AccountSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        child = value.get_child()
        if isinstance(child, BankAccount):
            serializer = BankAccountSerializer(child)
        elif isinstance(child, Wallet):
            serializer = WalletSerializer(child)
        elif isinstance(child, CreditCard):
            serializer = CreditCardSerializer(child)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data

    class Meta:
        model = Account
        fields = ("id",)


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('__all__')


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('__all__')


class CreditCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditCard
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class ExpenseSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    account_id = serializers.UUIDField(write_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Expense
        fields = ('__all__')


class IncomeSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    account_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Income
        fields = ("__all__")


class TransferSerializer(serializers.ModelSerializer):
    account_from = AccountSerializer(read_only=True)
    account_to = AccountSerializer(read_only=True)
    account_from_id = serializers.UUIDField(write_only=True)
    account_to_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Transfer
        fields = "__all__"

    def validate(self, data):
        account_from_id = data.get("account_from_id", self.instance.account_from_id)
        account_to_id = data.get("account_to_id", self.instance.account_to_id)
        if account_from_id == account_to_id:
            raise serializers.ValidationError("You can't transfer to the same account")
        return data


class CategoryMonthSerializer(serializers.ModelSerializer):
    used = serializers.SerializerMethodField("used_amount", read_only=True)

    def used_amount(self, category):
        return sum(i.amount for i in category.expenses_month)

    class Meta:
        model = Category
        fields = "__all__"
