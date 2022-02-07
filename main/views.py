from django.shortcuts import render
from .models import Products

def Index(request):
    products = Products.objects.all()

    return render(request,'index.html',{
        'product2': products
    })

def About(request):
    return render(request,'about.html')

def Product(request):
    product = Products.objects.all()

    return render(request,'products.html',{
        'products': product
    })

def Contact(request):
    return render(request,'contact.html')


