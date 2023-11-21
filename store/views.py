from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('collections').all()
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     return Product.objects.select_related('collections').all()
    
    # def get_serializer(self, *args, **kwargs):
    #     # don't return ProductSerializer()
    #     return ProductSerializer 
    
    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response({'error':'Product cannot be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


class CollectionList(generics.ListCreateAPIView):
    queryset = Collection.objects.annotate(products_count=Count('products')).all().order_by('id')
    serializer_class = CollectionSerializer
    

class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collection can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
