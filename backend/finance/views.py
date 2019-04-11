from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WalletSerializers, SourceSerializers, CreditCardSerializers, BankAccountSerializers, ExpensesSerializers, IncomesSerializers, TransferSerializers
from .models import Wallet, Source, CreditCard, BankAccount, Expenses, Incomes, Transfer

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
    serializer_class = ExpensesSerializers
    queryset = Expenses.objects.all()

class IncomesView(viewsets.ModelViewSet):
    serializer_class = IncomesSerializers
    queryset = Incomes.objects.all()

class TransferView(viewsets.ModelViewSet):
    serializer_class = TransferSerializers
    queryset = Transfer.objects.all()