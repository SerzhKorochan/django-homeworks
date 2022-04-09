import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings

DATA = []

with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    DATA = list(reader)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    pages = Paginator(DATA, 10)
    page_num = int(request.GET.get('page', 1))

    current_page = pages.page(page_num)

    context = {
        'bus_stations': current_page,
        'page': current_page,
    }

    return render(request, 'stations/index.html', context)
