from django.shortcuts import render
from django.core.paginator import Paginator

# вьюхи - функции - контроллеры
from mainapp.models import Product, ProductCategory



def index(request):
    context = {
        'title': 'Shop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
    else:
        products = Product.objects.all()
    paginator = Paginator(products, per_page=6)
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})

    return render(request, 'mainapp/products.html', context)

def base(request):
    return render(request, 'mainapp/base.html')



