from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WalletSerializers, SourceSerializers
from .models import Wallet, Source

class SourceView(viewsets.ModelViewSet):
    serializer_class = SourceSerializers
    queryset = Wallet.objects.all()

class WalletView(viewsets.ModelViewSet):
    serializer_class = WalletSerializers
    queryset = Wallet.objects.all()