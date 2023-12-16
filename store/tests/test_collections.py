from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestCreateCollection:
    def test_user_if_anonymous_returns_401(self):
        # AAA(arrange, act, assert)
        
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED