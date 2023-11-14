from django.urls import path
from . import views

# Urlconfig
urlpatterns = [
    path('hello/',views.say_hello, name='say_hello'),
    path('sql/', views.debug, name='debug'),
]