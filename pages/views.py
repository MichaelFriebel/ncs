from django.shortcuts import render
from django.http import HttpResponse
# from reservation.dates import available_dates

def index(request):
    # template = 'home/home.html'
    # context = {
    #     'available_dates': available_dates,
    # }
    return render(request, 'pages/index.html')


def about(request):
    # template = 'home/home.html'
    return render(request, 'pages/about.html')


def contact(request):
    template = 'pages/contact.html'
    # context = {}
    return render(request, template)


def gallery(request):
    template = 'pages/gallery.html'
    # context = {}
    return render(request , template)