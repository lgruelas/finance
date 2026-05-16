from datetime import date
from decimal import Decimal

from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Account, Category, Expense, Income, Institution, Transfer
from .serializers import (
    AccountSerializer,
    BudgetSerializer,
    CategorySerializer,
    ExpenseSerializer,
    IncomeSerializer,
    InstitutionSerializer,
    RegisterSerializer,
    SummarySerializer,
    TransferSerializer,
)


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class InstitutionViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Institution.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["account_type", "institution"]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user).select_related("institution")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["category_type"]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["account", "category", "is_paid", "date"]
    ordering_fields = ["date", "amount"]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user).select_related("account", "category")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["account", "category", "is_paid", "date"]
    ordering_fields = ["date", "amount"]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).select_related("account", "category")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransferViewSet(viewsets.ModelViewSet):
    serializer_class = TransferSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["account_from", "account_to", "is_paid", "date"]
    ordering_fields = ["date", "amount"]

    def get_queryset(self):
        return Transfer.objects.filter(user=self.request.user).select_related("account_from", "account_to")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SummaryView(RetrieveAPIView):
    serializer_class = SummarySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        accounts = Account.objects.filter(user=user)

        by_type = []
        total = Decimal("0")
        for at in Account.AccountType.values:
            group = accounts.filter(account_type=at)
            if not group.exists():
                continue
            agg = group.aggregate(total=Sum("balance"))["total"] or Decimal("0")
            count = group.count()
            by_type.append({
                "account_type": at,
                "total_balance": agg,
                "count": count,
            })
            if at == Account.AccountType.CREDIT_CARD:
                total -= agg
            else:
                total += agg

        return {"total_balance": total, "by_type": by_type}


class BudgetView(RetrieveAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        today = date.today()
        year = int(self.request.query_params.get("year", today.year))
        month = int(self.request.query_params.get("month", today.month))

        expense_categories = Category.objects.filter(
            user=user, category_type=Category.CategoryType.EXPENSE
        )

        categories_data = []
        total_spent = Decimal("0")
        total_budget = Decimal("0")

        for cat in expense_categories:
            spent = Expense.objects.filter(
                user=user,
                category=cat,
                date__year=year,
                date__month=month,
            ).aggregate(total=Sum("amount"))["total"] or Decimal("0")

            budget = cat.monthly_budget or Decimal("0")
            percentage = float(spent / budget * 100) if budget else 0.0

            categories_data.append({
                "category_id": cat.id,
                "category_name": cat.name,
                "monthly_budget": budget,
                "spent": spent,
                "percentage": percentage,
            })
            total_spent += spent
            total_budget += budget

        return {
            "year": year,
            "month": month,
            "total_spent": total_spent,
            "total_budget": total_budget,
            "categories": categories_data,
        }
