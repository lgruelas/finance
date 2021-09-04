from rest_framework import routers
from django.urls import path, include

from .views import (WalletView, CreditCardView, BankAccountView, ExpenseView,
                    IncomeView, TransferView, CategoryView, CategoryByMonthView)

router = routers.DefaultRouter()
router.register(r'wallets', WalletView, 'wallet')
router.register(r'cards', CreditCardView, 'credit_card')
router.register(r'bank-accounts', BankAccountView, 'bank_accounts')
router.register(r'expenses', ExpenseView, 'expenses')
router.register(r'incomes', IncomeView, 'incomes')
router.register(r'transfers', TransferView, 'transfers')
router.register(r'categories', CategoryView, 'categories')

urlpatterns = [

    path('', include(router.urls)),

    path('categories-spent/<int:year>/<int:month>/', CategoryByMonthView.as_view({"get": "list"})),
    path('categories-spent/<uuid:pk>/<int:year>/<int:month>/', CategoryByMonthView.as_view({"get": "retrieve"}))
]
