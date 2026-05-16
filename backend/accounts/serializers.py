from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.db.models import Sum
from django.utils.dateparse import parse_date

from .models import Account, Category, Expense, Income, Institution, Transfer, User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ["id", "name", "image", "date_created"]
        read_only_fields = ["id", "date_created"]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "institution",
            "account_type",
            "name",
            "balance",
            "cut_date",
            "pay_date",
            "credit_limit",
            "is_payroll",
            "investment_return",
            "date_created",
        ]
        read_only_fields = ["id", "date_created"]

    def validate(self, data):
        account_type = data.get("account_type")
        if account_type is None and self.instance:
            account_type = self.instance.account_type

        required_by_type = {
            Account.AccountType.CREDIT_CARD: {"cut_date", "pay_date", "credit_limit"},
            Account.AccountType.SAVINGS: {"is_payroll"},
            Account.AccountType.INVESTMENT: {"investment_return"},
        }
        forbidden_by_type = {
            Account.AccountType.CREDIT_CARD: {"is_payroll", "investment_return"},
            Account.AccountType.SAVINGS: {"cut_date", "pay_date", "credit_limit", "investment_return"},
            Account.AccountType.INVESTMENT: {"cut_date", "pay_date", "credit_limit", "is_payroll"},
        }

        if account_type not in required_by_type:
            raise serializers.ValidationError({"account_type": "Invalid account type."})

        required = required_by_type[account_type]
        forbidden = forbidden_by_type[account_type]

        # On PATCH, only validate fields the client explicitly sent
        if self.partial:
            incoming = set(self.initial_data.keys())
            missing = required & incoming - {k for k, v in data.items() if v is not None}
        else:
            missing = required - {k for k, v in data.items() if v is not None}

        if missing:
            raise serializers.ValidationError(
                {f: f"This field is required for {account_type} accounts." for f in missing}
            )

        for f in forbidden:
            if f in data and data[f] is not None:
                raise serializers.ValidationError(
                    {f: f"This field must be null for {account_type} accounts."}
                )
            data[f] = None

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_type", "name", "monthly_budget", "date_created"]
        read_only_fields = ["id", "date_created"]

    def validate(self, data):
        if self.instance and "category_type" in data:
            has_transactions = (
                self.instance.incomes.exists() or self.instance.expenses.exists()
            )
            if has_transactions:
                raise serializers.ValidationError(
                    {"category_type": "Cannot change type of a category with associated transactions."}
                )
        return data


class _user_account:
    """Mixin for serializers that need to validate account ownership and category type."""

    def _validate_account_ownership(self, value):
        if value.user != self.context["request"].user:
            raise serializers.ValidationError("Account does not belong to this user.")
        return value


class IncomeSerializer(_user_account, serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ["id", "account", "category", "amount", "is_paid", "description", "date", "date_created"]
        read_only_fields = ["id", "date_created"]

    def validate_account(self, value):
        if value.user != self.context["request"].user:
            raise serializers.ValidationError("Account does not belong to this user.")
        return value

    def validate_category(self, value):
        if value.category_type != Category.CategoryType.INCOME:
            raise serializers.ValidationError("Category must be of type INCOME.")
        if value.user != self.context["request"].user:
            raise serializers.ValidationError("Category does not belong to this user.")
        return value


class ExpenseSerializer(_user_account, serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "account", "category", "amount", "is_paid", "description", "date", "date_created"]
        read_only_fields = ["id", "date_created"]

    def validate_account(self, value):
        if value.user != self.context["request"].user:
            raise serializers.ValidationError("Account does not belong to this user.")
        return value

    def validate_category(self, value):
        if value.category_type != Category.CategoryType.EXPENSE:
            raise serializers.ValidationError("Category must be of type EXPENSE.")
        if value.user != self.context["request"].user:
            raise serializers.ValidationError("Category does not belong to this user.")
        return value


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ["id", "account_from", "account_to", "amount", "is_paid", "description", "date", "date_created"]
        read_only_fields = ["id", "date_created"]

    def validate(self, data):
        if data["account_from"] == data["account_to"]:
            raise serializers.ValidationError("Source and destination accounts must be different.")
        user = self.context["request"].user
        if data["account_from"].user != user:
            raise serializers.ValidationError({"account_from": "Account does not belong to this user."})
        if data["account_to"].user != user:
            raise serializers.ValidationError({"account_to": "Account does not belong to this user."})
        return data


class AccountSummarySerializer(serializers.Serializer):
    account_type = serializers.CharField()
    total_balance = serializers.DecimalField(decimal_places=4, max_digits=12)
    count = serializers.IntegerField()


class SummarySerializer(serializers.Serializer):
    total_balance = serializers.DecimalField(decimal_places=4, max_digits=12)
    by_type = AccountSummarySerializer(many=True)


class CategoryBudgetSerializer(serializers.Serializer):
    category_id = serializers.UUIDField()
    category_name = serializers.CharField()
    monthly_budget = serializers.DecimalField(decimal_places=4, max_digits=12, allow_null=True)
    spent = serializers.DecimalField(decimal_places=4, max_digits=12)
    percentage = serializers.FloatField()


class BudgetSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    total_spent = serializers.DecimalField(decimal_places=4, max_digits=12)
    total_budget = serializers.DecimalField(decimal_places=4, max_digits=12)
    categories = CategoryBudgetSerializer(many=True)
