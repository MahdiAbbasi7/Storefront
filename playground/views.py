from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Mahdi'})