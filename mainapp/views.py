from django.shortcuts import render

# вьюхи - функции - контроллеры
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Shop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, id=None):
    context = {
            'title': 'Shop - Каталог',
            'products': Product.objects.all(),
            'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)

def base(request):
    return render(request, 'mainapp/base.html')