"""
URL configuration for the core app.
"""

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('brand-guidelines/', views.brand_guidelines, name='brand_guidelines'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]
