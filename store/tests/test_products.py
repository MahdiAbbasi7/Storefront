from decimal import Decimal
from rest_framework import status
from model_bakery import baker
from store.models import Product, Collection
import pytest


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_user_if_anonymous_returns_401(self, create_product):
        response = create_product({'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_user_is_not_admin_return_403(self, create_product, auth_client):
        auth_client()

        response = create_product({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_data_is_not_valid_returns_400(self, create_product, auth_client):
        auth_client(is_staff=True)

        response = create_product({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_data_is_valid_returns_201(self, create_product, auth_client):
        auth_client(is_staff=True)

        collection = baker.make(Collection) # create a Collection object

        response = create_product({
            'title':'a',
            'slug':'-',
            'inventory_type':5, 
            'collections': collection.id,
            'price':93.6,
            'description':'a'
        })

        print(response.data)

        assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_product_exists_returns_200(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": product.id,
            "title": product.title,
            "slug": product.slug,
            "inventory_type": product.inventory_type,
            "collections": product.collections.id,
            "price": Decimal(product.price),
            "price_with_tax": product.price * Decimal(1.1),
            "description": product.description,
            'images':[]
        }