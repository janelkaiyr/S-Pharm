from django.db.models import Min
from django.shortcuts import render, redirect
from .models import Drugs, Pharmacies, Apteks
from .forms import DocumentForm, RecommendForm, DeliveryForm
from django.core.mail import send_mail
from .forms import SearchForm
import folium
import geocoder


def index(request):
    return render(request, 'main/index.html')


def index2(request):
    return render(request, 'main/index2.html')


def delivery(request):
    return render(request, 'main/delivery.html')


def map(request):
    pharm = Apteks.objects.order_by('-id')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/map')
    else:
        form = SearchForm()
    address = Pharmacies.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[19.0, -12.1], zoom_start=2)
    folium.Marker([19.0, -12.1], tooltip='Узнай больше', popup=country).add_to(m)
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
        'pharmacy': pharm
    }
    return render(request, 'main/map.html', context)


def drugs(request):
    drugs = Drugs.objects.order_by('-id')
    return render(request, 'main/drugs.html', {'title': 'Все лекарства', 'drugs': drugs})


def analogies(request):
    drug = Drugs.objects.order_by('id')
    return render(request, 'main/analogies.html', {'title': 'Все лекарства', 'drug': drug})


def pharmacy(request):
    return render(request, 'main/pharmacy.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = DocumentForm()
    return render(request, 'main/model.html', {
        'form': form
    })


def recommendations(request):
    if request.method == 'POST':
        form = RecommendForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = RecommendForm()
    return render(request, 'main/recommend.html', {
        'form': form
    })


def Delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "main/index.html")
    else:
        form = DeliveryForm()
    return render(request, 'main/delivery.html', {
        'form': form
    })
