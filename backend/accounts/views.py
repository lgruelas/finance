from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Account, Category, Expense, Income, Institution, Transfer
from .serializers import (
    AccountSerializer,
    CategorySerializer,
    ExpenseSerializer,
    IncomeSerializer,
    InstitutionSerializer,
    RegisterSerializer,
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
