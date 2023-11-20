from decimal import Decimal
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    inventory = serializers.IntegerField(source='inventory_type')
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_price_with_tax')

    def calculate_price_with_tax(self,product: Product):
        return product.price * Decimal(1.1)