from django.urls import path
from . import views

# Urlconfig
urlpatterns = [
    path('hello/',views.HelloView.as_view(), name='say_hello'),
    # path('sql/', views.debug, name='debug'),
]