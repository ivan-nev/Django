from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv
from django.core.paginator import Paginator

with open(BUS_STATION_CSV, encoding='UTF8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    bus_stations_list = []
    for row in reader:
        bus_stations_list.append(
            {'Name': row['Name'], 'Street': row['Street'], 'District': row['District'], 'ID': row['ID']})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    count = 15
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_list, count)
    page = paginator.get_page(page_num)
    data = page.object_list

    context = {
        'bus_stations': data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
