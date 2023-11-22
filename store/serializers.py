from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection, Review
from django.db.models import Count


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
        
    products_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug','inventory_type','collections',
                  'price', 'price_with_tax', 'description']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_price_with_tax')
    
    def calculate_price_with_tax(self,product: Product):
        return product.price * Decimal(1.1)
    
class ReveiwSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'data', 'name', 'descriptions']

        def create(self, validated_data):
            product_id = self.context['product_id']
            return Review.objects.create(product_id=product_id, **validated_data)