from django.shortcuts import render

# вьюхи - функции - контроллеры
from mainapp.models import Product, ProductCategory



def index(request):
    context = {
        'title': 'Shop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, category_id=None):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        context.update({'products': Product.objects.filter(category_id=category_id)})
    else:
        context.update({'products': Product.objects.all()})
    return render(request, 'mainapp/products.html', context)

def base(request):
    return render(request, 'mainapp/base.html')

