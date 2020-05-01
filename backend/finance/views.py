from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import (WalletSerializers, SourceSerializers, CreditCardSerializers,
                          BankAccountSerializers, ExpenseSerializers, IncomeSerializers,
                          TransferSerializers, CategorySerializers)
from .methods import get_account_instance
from .models import Source, Wallet, BankAccount, CreditCard, Expense, Income, Category, Transfer
from decimal import Decimal


class SourceView(viewsets.ModelViewSet):
    serializer_class = SourceSerializers
    queryset = Source.objects.all()


class WalletView(viewsets.ModelViewSet):
    serializer_class = WalletSerializers
    queryset = Wallet.objects.all()


class CreditCardView(viewsets.ModelViewSet):
    serializer_class = CreditCardSerializers
    queryset = CreditCard.objects.all()


class BankAccountView(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializers
    queryset = BankAccount.objects.all()


class ExpenseView(viewsets.ModelViewSet):
    def create(self, request):
        expense = ExpenseSerializers(data=request.data)
        if expense.is_valid():
            account, type_ = get_account_instance(request.data.get('account'))
            if type_ == "CreditCard":
                account.used += Decimal(request.data.get('amount'))
            else:
                account.balance -= Decimal(request.data.get('amount'))
            account.save()
            expense.save()
            return Response(
                {"success": "Expense '{}' created successfully".format(request.data.get('description'))},
                status=201
            )
        else:
            return Response({"error": "Expense not added"}, status=400)

    serializer_class = ExpenseSerializers
    queryset = Expense.objects.all()


class IncomeView(viewsets.ModelViewSet):
    serializer_class = IncomeSerializers
    queryset = Income.objects.all()

    def create(self, request):
        income = IncomeSerializers(data=request.data)
        if income.is_valid():
            account, type_ = get_account_instance(request.data.get('account'))
            if type_ == "CreditCard":
                account.used -= Decimal(request.data.get('amount'))
            else:
                account.balance += Decimal(request.data.get('amount'))
            account.save()
            income.save()
            return Response(
                {"success": "Income '{}' created successfully".format(request.data.get('description'))},
                status=201
            )
        else:
            return Response({"error": "Income not added"}, status=400)


class TransferView(viewsets.ModelViewSet):
    def create(self, request):
        transfer = TransferSerializers(data=request.data)
        if transfer.is_valid():
            account_from, account_from_type = get_account_instance(request.data.get('account_from'))
            account_to, account_to_type = get_account_instance(request.data.get('account_to'))
            if account_from_type == "CreditCard":
                return Response({"error": "for now you can't transfer from credit card"}, status=403)
            account_from.balance -= Decimal(request.data.get('amount'))
            if account_to_type == "CreditCard":
                account_to.used -= Decimal(request.data.get('amount'))
            else:
                account_to.balance += Decimal(request.data.get('amount'))
            transfer.save()
            account_from.save()
            account_to.save()
            return Response(
                {
                    "success": "Transfer of '{}', '{}' => '{}' created"
                    "successfully".format(request.data.get('amount'), account_from, account_to)
                },
                status=201)
        else:
            return Response({"error": "Transfer not added"}, status=400)

    serializer_class = TransferSerializers
    queryset = Transfer.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
