from django.shortcuts import render

# вьюхи - функции - контроллеры

def index(request):
    context = {'title': 'Shop'}
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {'title': 'Shop - Каталог'}
    return render(request, 'mainapp/products.html', context)

def base(request):
    return render(request, 'mainapp/base.html')