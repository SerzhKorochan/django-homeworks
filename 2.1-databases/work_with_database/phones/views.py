from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')

    if sort: 
        phones = phones.order_by(SORT_MAP[sort])

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
