from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def price(request):
    return render(request, 'price.html')

def service(request):
    return render(request, 'service.html')
# Create your views here.
