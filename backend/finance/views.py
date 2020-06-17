from decimal import Decimal
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.db.models import Prefetch
from django.shortcuts import get_object_or_404

from .serializers import (WalletSerializer, CreditCardSerializer,
                          BankAccountSerializer, ExpenseSerializer, IncomeSerializer,
                          TransferSerializer, CategorySerializer,
                          CategoryMonthSerializer)
from .models import Account, Wallet, BankAccount, CreditCard, Expense, Income, Category, Transfer


class WalletView(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class CreditCardView(viewsets.ModelViewSet):
    serializer_class = CreditCardSerializer
    queryset = CreditCard.objects.all()


class BankAccountView(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()


class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    def create(self, request):
        expense = ExpenseSerializer(data=request.data)
        if expense.is_valid():
            account = get_object_or_404(Account, id=request.data['account_id'])
            account.balance -= Decimal(request.data.get('amount'))
            account.save()
            expense.save()
            return Response(
                {"success": "Expense '{}' created successfully".format(request.data.get('description'))},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({"error": "Expense not added, error in {}".format(
                ", ".join(expense.errors.keys())
            )}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        accounts_update = []

        if "account_id" in serializer.validated_data and instance.account_id != serializer.validated_data["account_id"]:
            instance.account.balance += instance.amount
            accounts_update.append(instance.account)
            instance.account = get_object_or_404(Account, id=serializer.validated_data["account_id"])
            instance.account.balance -= instance.amount

        if "amount" in serializer.validated_data and instance.amount != serializer.validated_data["amount"]:
            diff = instance.amount - serializer.validated_data["amount"]
            instance.account.balance += diff

        accounts_update.extend([instance.account])
        Account.objects.bulk_update(accounts_update, ['balance'])
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        expense = self.get_object()
        expense.account.balance += expense.amount
        expense.account.save()
        self.perform_destroy(expense)
        return Response(status=status.HTTP_204_NO_CONTENT)



class IncomeView(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()

    def create(self, request):
        income = IncomeSerializer(data=request.data)
        if income.is_valid():
            account = get_object_or_404(Account, id=request.data['account_id'])
            account.balance += Decimal(request.data.get('amount'))
            account.save()
            income.save()
            return Response(
                {"success": "Income '{}' created successfully".format(request.data.get('description'))},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({"error": "Income not added, error in {}".format(
                ", ".join(income.errors.keys())
            )}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        accounts_update = []

        if "account_id" in serializer.validated_data and instance.account_id != serializer.validated_data["account_id"]:
            instance.account.balance -= instance.amount
            accounts_update.append(instance.account)
            instance.account = get_object_or_404(Account, id=serializer.validated_data["account_id"])
            instance.account.balance += instance.amount

        if "amount" in serializer.validated_data and instance.amount != serializer.validated_data["amount"]:
            diff = instance.amount - serializer.validated_data["amount"]
            instance.account.balance -= diff

        accounts_update.extend([instance.account])
        Account.objects.bulk_update(accounts_update, ['balance'])
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        income = self.get_object()
        income.account.balance -= income.amount
        income.account.save()
        self.perform_destroy(income)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransferView(viewsets.ModelViewSet):
    serializer_class = TransferSerializer
    queryset = Transfer.objects.all()

    def create(self, request):
        transfer = TransferSerializer(data=request.data)
        if transfer.is_valid():
            account_from = get_object_or_404(Account, id=request.data['account_from_id'])
            account_to = get_object_or_404(Account, id=request.data['account_to_id'])
            if isinstance(account_from, CreditCard):
                return Response({"error": "for now you can't transfer from credit card"}, status=403)
            account_from.balance -= Decimal(request.data['amount'])
            account_to.balance += Decimal(request.data['amount'])
            transfer.save()
            account_from.save()
            account_to.save()
            return Response(
                {
                    "success": "Transfer of '{}', '{}' => '{}' created "
                    "successfully".format(request.data['amount'], account_from, account_to)
                },
                status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Transfer not added, error in {}".format(
                ", ".join(transfer.errors.keys())
            )}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        accounts_update = []
        if "account_from_id" in serializer.validated_data and instance.account_from_id != serializer.validated_data["account_from_id"]:
            instance.account_from.balance += instance.amount
            accounts_update.append(instance.account_from)
            instance.account_from = get_object_or_404(Account, id=serializer.validated_data["account_from_id"])
            instance.account_from.balance -= instance.amount

        if "account_to_id" in serializer.validated_data and instance.account_to_id != serializer.validated_data["account_to_id"]:
            instance.account_to.balance -= instance.amount
            accounts_update.append(instance.account_to)
            instance.account_to = get_object_or_404(Account, id=serializer.validated_data["account_to_id"])
            instance.account_to.balance += instance.amount

        if "amount" in serializer.validated_data and instance.amount != serializer.validated_data["amount"]:
            diff = instance.amount - serializer.validated_data["amount"]
            instance.account_from.balance += diff
            instance.account_to.balance -= diff

        accounts_update.extend([instance.account_from, instance.account_to])
        Account.objects.bulk_update(accounts_update, ['balance'])
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        transfer = self.get_object()
        transfer.account_from.balance += transfer.amount
        transfer.account_to.balance -= transfer.amount
        transfer.account_from.save()
        transfer.account_to.save()
        self.perform_destroy(transfer)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryByMonthView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoryMonthSerializer

    def get_queryset(self):
        month = self.kwargs["month"]
        year = self.kwargs["year"]
        prefetch = Prefetch("expenses",
            queryset=Expense.objects.filter(date__month=month, date__year=year),
            to_attr="expenses_month"
        )
        return Category.objects.prefetch_related(prefetch).filter(must_show=True)
