from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import WalletSerializers, SourceSerializers, CreditCardSerializers, BankAccountSerializers, ExpensesSerializers, IncomesSerializers, TransferSerializers, CategorySerializers
from .models import Wallet, Source, CreditCard, BankAccount, Expenses, Incomes, Transfer, Category

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
        account_id = request.data.get('account')
        try:
            account = BankAccount.objects.get(source__id=account_id)
            account.balance -= request.data.get('amount')
            account.save()
        except BankAccount.DoesNotExist:
            try:
                account = CreditCard.objects.get(source__id=account_id)
                account.used += request.data.get('amount')
                account.save()
            except CreditCard.DoesNotExist:
                account = Wallet.objects.get(source__id=account_id)
                account.balance -= request.data.get('amount')
                account.save()
        return Response({"success": "Expense '{}' created successfully".format(request.data.get('description'))})

    serializer_class = ExpensesSerializers
    queryset = Expenses.objects.all()

class IncomesView(viewsets.ModelViewSet):
    serializer_class = IncomesSerializers
    queryset = Incomes.objects.all()

class TransferView(viewsets.ModelViewSet):
    serializer_class = TransferSerializers
    queryset = Transfer.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()