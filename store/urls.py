from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('collections/', views.CollectionList.as_view(), name='collection_list'),
    path('products/<int:id>', views.ProductDetail.as_view(), name='product_detail'),
    path('collections/<int:id>', views.collection_detail, name = 'collections-detail'),
]
