from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('collections/', views.CollectionList.as_view(), name='collection_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('collections/<int:pk>', views.CollectionDetail.as_view(), name = 'collections-detail'),
]
