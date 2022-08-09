from django.shortcuts import render
from django.core.paginator import Paginator

from .models import *

def home(request):
    news = News.objects.order_by("-id")[:4]
    doctors = Doctor.objects.order_by("-id")
    partners = Partner.objects.order_by("-id")
    images = Image.objects.order_by("-id")

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


def doctors(request):
    doctors = Doctor.objects.order_by("id")

    return render(request, 'doctors.html', {
        'doctors': doctors
    })
    
def services(request):
    services = Service.objects.order_by("id")

    return render(request, 'services.html', {
        'services': services
    })

def about(request):
    about = About.objects.all()

    return render(request, 'about.html', {
        'about': about
    })

def ourpartners(request):
    partners = Partner.objects.all()

    return render(request, 'ourpartners.html', {
        'partners': partners
    })

def fotogalereya(request):
    fotogalereya = Image.objects.order_by("-id")

    return render(request, 'fotogalereya.html', {
        'fotogalereya': fotogalereya
    })

