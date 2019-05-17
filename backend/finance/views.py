from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import WalletSerializers, SourceSerializers, CreditCardSerializers, BankAccountSerializers, ExpensesSerializers, IncomesSerializers, TransferSerializers, CategorySerializers
from .methods import get_account_instance
from .models import Source, Wallet, BankAccount, CreditCard, Expenses, Incomes, Category, Transfer
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

class ExpensesView(viewsets.ModelViewSet):
    def create(self, request):
        account, type_ = get_account_instance(request.data.get('account'))
        if type_ == "CreditCard":
            account.used += Decimal(request.data.get('amount'))
        else:
            account.balance -= Decimal(request.data.get('amount'))
        account.save()
        return Response({"success": "Expense '{}' created successfully".format(request.data.get('description'))})

    serializer_class = ExpensesSerializers
    queryset = Expenses.objects.all()

class IncomesView(viewsets.ModelViewSet):
    serializer_class = IncomesSerializers
    queryset = Incomes.objects.all()

class TransferView(viewsets.ModelViewSet):
    def create(self, request):
        account_from, account_from_type = get_account_instance(request.data.get('account_from'))
        account_to, account_to_type = get_account_instance(request.data.get('account_to'))
        if account_from_type == "CreditCard":
            return Response({"error": "for now you can't transfer from credit card"}, status=403)
        account_from.balance -= Decimal(request.data.get('amount'))
        if account_to_type == "CreditCard":
            account_to.used -= Decimal(request.data.get('amount'))
        else:
            account_to.balance += Decimal(request.data.get('amount'))
        account_from.save()
        account_to.save()
        return Response({"success": "Transfer of '{}', '{}' => '{}' created successfully".format(request.data.get('amount'), account_from, account_to)})


    serializer_class = TransferSerializers
    queryset = Transfer.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()