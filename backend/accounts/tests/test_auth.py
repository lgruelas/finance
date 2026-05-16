import pytest
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.factories import UserFactory

User = get_user_model()

REGISTER_URL = "/api/v1/auth/register/"
LOGIN_URL = "/api/v1/auth/login/"
REFRESH_URL = "/api/v1/auth/refresh/"


@pytest.mark.django_db
class TestRegistration:
    def test_register_user(self, api_client):
        data = {"username": "newuser", "email": "new@test.com", "password": "strongpass123"}
        response = api_client.post(REGISTER_URL, data, format="json")
        assert response.status_code == 201
        assert User.objects.filter(username="newuser").exists()

    def test_register_duplicate_username(self, api_client):
        UserFactory(username="taken")
        data = {"username": "taken", "email": "other@test.com", "password": "strongpass123"}
        response = api_client.post(REGISTER_URL, data, format="json")
        assert response.status_code == 400


@pytest.mark.django_db
class TestLogin:
    def test_login_returns_tokens(self, api_client):
        user = UserFactory(username="loginuser")
        data = {"username": "loginuser", "password": "testpass123"}
        response = api_client.post(LOGIN_URL, data, format="json")
        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data

    def test_login_invalid_credentials(self, api_client):
        UserFactory(username="loginuser")
        data = {"username": "loginuser", "password": "wrongpass"}
        response = api_client.post(LOGIN_URL, data, format="json")
        assert response.status_code == 401


@pytest.mark.django_db
class TestRefreshToken:
    def test_refresh_returns_new_access(self, api_client):
        user = UserFactory(username="refreshuser")
        refresh = RefreshToken.for_user(user)
        response = api_client.post(REFRESH_URL, {"refresh": str(refresh)}, format="json")
        assert response.status_code == 200
        assert "access" in response.data
