from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import (
    AccountViewSet,
    CategoryViewSet,
    ExpenseViewSet,
    IncomeViewSet,
    InstitutionViewSet,
    RegisterView,
    TransferViewSet,
)

router = DefaultRouter()
router.register(r"institutions", InstitutionViewSet, basename="institution")
router.register(r"accounts", AccountViewSet, basename="account")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"incomes", IncomeViewSet, basename="income")
router.register(r"expenses", ExpenseViewSet, basename="expense")
router.register(r"transfers", TransferViewSet, basename="transfer")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/register/", RegisterView.as_view(), name="auth-register"),
    path("api/v1/auth/login/", TokenObtainPairView.as_view(), name="auth-login"),
    path("api/v1/auth/refresh/", TokenRefreshView.as_view(), name="auth-refresh"),
    path("api/v1/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
