from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields=['id', 'title']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'inventory_type','collections','price', 'price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_price_with_tax')
    collections = serializers.HyperlinkedRelatedField(
        view_name='collections-detail',
        queryset = Collection.objects.all()
    )
    def calculate_price_with_tax(self,product: Product):
        return product.price * Decimal(1.1)