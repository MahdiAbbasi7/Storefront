from django.contrib.auth.models import User
from rest_framework import status
from model_bakery import baker
from store.models import Collection
import pytest

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_user_if_anonymous_returns_401(self, create_collection):
        # AAA(arrange, act, assert)
        response = create_collection({'title':'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_user_if_not_admin_returns_403(self, create_collection, auth_client):
        # Arrange
        auth_client()

        # Act
        response = create_collection({'title':'a'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_data_is_not_valid_returns_400(self, create_collection, auth_client):
        auth_client(is_staff=True)

        response = create_collection({'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_data_is_valid_returns_201(self, create_collection, auth_client):
        auth_client(is_staff=True)

        response = create_collection({'title':'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        # api_client.post('store/collection')
        collection = baker.make(Collection)

        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0,
        }

        


 