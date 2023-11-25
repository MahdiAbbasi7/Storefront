from decimal import Decimal
from rest_framework import serializers
from .models import CartItem, Product, Collection, Review, Cart
from django.db.models import Count
from uuid import uuid4


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

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','price']


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.price
    
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_price']
    
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        return sum([item.quantity * item.product.price for item in cart.items.all() if item])

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']
        read_only_fields = ['id']

            

    def create(self, validated_data):
        validated_data['id'] = uuid4()
        return super().create(validated_data)
