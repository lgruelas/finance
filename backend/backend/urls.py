"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from finance import views

router = routers.DefaultRouter()
router.register(r'wallets', views.WalletView, 'wallet')
router.register(r'cards', views.CreditCardView, 'credit_card')
router.register(r'accounts', views.BankAccountView, 'bank_accounts')
router.register(r'expenses', views.ExpensesView, 'expenses')
router.register(r'incomes', views.IncomesView, 'incomes')
router.register(r'transfers', views.TransferView, 'transfers')
router.register(r'categories', views.CategoryView, 'categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
