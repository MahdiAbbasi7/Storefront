from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_hello(request):
    query_set = Product.objects.all()
    for product in query_set :
        print(product)
    return render(request, 'hello.html', {'name': 'Mahdi'})

def debug(request):
    # None : if we use first()
    # Boolean : if we use exists()
    query_set = Product.objects.filter(price__range=(200, 300))
    return render(request, 'sqll.html', {'products': list(query_set)})