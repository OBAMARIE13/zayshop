from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('shop/', views.shop, name = 'shop'),
    path('shopsingle/', views.shopsingle, name = 'shopsingle'),
    path('contact/', views.contact, name = 'contact'),
    path('post-newsletter/', views.newsletterpost, name = 'newsletterpost'),
]