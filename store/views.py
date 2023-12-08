from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, \
                                    DestroyModelMixin,RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from store.permissions import IsAdminOrReadOnly
from .filters import ProductFilter
from .models import Customer, Product, Collection, OrderItem, Review, Cart, CartItem
from .serializers import CustomerSerializer, ProductSerializer, CollectionSerializer , \
                        ReveiwSerializer, CartSerializer, \
                        CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Customer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    permission_classes =[IsAdminOrReadOnly]
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'last_updated']

    def get_serializer_context(self):
        return {'request': self.request}
    

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error':'Product cannot be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)     



class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collections_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)            
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReveiwSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
    

class CartViewSet(ListModelMixin,
                  CreateModelMixin,
                  DestroyModelMixin,
                  RetrieveModelMixin,
                  GenericViewSet):
    
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    # serializer_class = CartItemSerializer
    http_method_names = ('get', 'post', 'delete', 'patch')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method=='PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
        

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk'],}

    def get_queryset(self):
        return CartItem.objects \
                .filter(cart_id=self.kwargs['cart_pk']) \
                .select_related('product')
    
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser] # list of permissions classes

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()] # list of permissions objects
    #     return [IsAuthenticated()]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer) = Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    # permission_classes =[IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer
    
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
    
    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()
        (customer_id, created) = Customer.objects.only('id').get_or_create(user_id=user.id)
        return Order.objects.filter(customer_id=customer_id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user = kwargs['instance'])
    def ready(self) -> None:
        import store.signals
customer_id = Customer.objects.only('id').get(user.id)
