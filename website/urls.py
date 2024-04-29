from django.urls import path
from .views import index, contact,price, about,service

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('price/', price, name='price'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
  
]