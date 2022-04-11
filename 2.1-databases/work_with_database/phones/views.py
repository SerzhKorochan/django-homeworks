from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    order_option = request.GET.get('sort')

    if order_option == 'name':
        phones = phones.order_by('name')
    elif order_option == 'min_price':
        phones = phones.order_by('price')
    elif order_option == 'max_price':
        phones = phones.order_by('-price')

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
