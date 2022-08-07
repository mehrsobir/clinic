from django.shortcuts import render
from django.core.paginator import Paginator

from .models import *

def home(request):
    news = News.objects.order_by("-id")[:4]
    doctors = Doctors.objects.order_by("-id")
    partners = Partners.objects.order_by("-id")
    images = Images.objects.order_by("-id")

    return render(request, 'home.html', {
        'news': news,
        'doctors': doctors,
        'partners': partners,
        'images': images
    })

def news(request):
    Pag = Paginator(News.objects.order_by("-id"), 2)
    page = request.GET.get('page')
    news = Pag.get_page(page)

    return render(request, 'news.html', {
        'news': news
    })

def services(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def about(request):
    return render(request, 'about.html')

def ourpartners(request):
    return render(request, 'ourpartners.html')

def fotogalereya(request):
    return render(request, 'fotogalereya.html')

