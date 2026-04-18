"""
Views for Smart Organics website.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import (
    Product, Service, Testimonial, TeamMember,
    CompanyStats, FAQ
)
from .forms import ContactForm, NewsletterForm


def home(request):
    """Home page with hero, services overview, stats, and testimonials."""
    context = {
        'page_title': 'Home',
        'meta_description': (
            'Smart Organics Limited — Kenya\'s trusted provider of certified coffee seedlings, '
            'organic agricultural inputs, and contract farming programs. '
            'Healthy Soil • Wealthy Farmers • Better Life.'
        ),
        'services': Service.objects.filter(is_featured=True)[:6],
        'products': Product.objects.filter(is_featured=True)[:3],
        'testimonials': Testimonial.objects.filter(is_featured=True)[:3],
        'stats': CompanyStats.objects.all()[:4],
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page with company profile, mission/vision, values, and team."""
    context = {
        'page_title': 'About Us',
        'meta_description': (
            'Learn about Smart Organics Limited — a Kenyan agribusiness company '
            'established in 2015, empowering smallholder farmers through sustainable '
            'agriculture since 2015.'
        ),
        'team_members': TeamMember.objects.filter(is_active=True),
        'stats': CompanyStats.objects.all()[:4],
    }
    return render(request, 'core/about.html', context)


def products(request):
    """Products page showcasing coffee seedlings, organic manure, and inputs."""
    context = {
        'page_title': 'Our Products',
        'meta_description': (
            'Explore Smart Organics\' range of certified coffee seedlings, '
            'organic manure, and agricultural inputs designed to boost farm productivity.'
        ),
        'products': Product.objects.all(),
        'seedlings': Product.objects.filter(category='seedlings'),
        'inputs': Product.objects.filter(category='inputs'),
        'manure': Product.objects.filter(category='manure'),
    }
    return render(request, 'core/products.html', context)


def services(request):
    """Services page covering contract farming, agronomy advisory, and training."""
    context = {
        'page_title': 'Our Services',
        'meta_description': (
            'Smart Organics offers contract coffee farming programs, professional '
            'agronomy advisory services, and farmer training programs across Kenya.'
        ),
        'services': Service.objects.all(),
        'faqs': FAQ.objects.filter(is_published=True)[:8],
    }
    return render(request, 'core/services.html', context)


def contact(request):
    """Contact page with form, map, and contact information."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for contacting us! We\'ll get back to you within 24 hours.'
            )
            return redirect('core:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'page_title': 'Contact Us',
        'meta_description': (
            'Get in touch with Smart Organics Limited. Located in Eldoret, Kenya. '
            'Call 0743 581 264 or email support@smartorganics.co.ke.'
        ),
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def brand_guidelines(request):
    """Brand guidelines page with logo usage, colors, typography, and imagery standards."""
    context = {
        'page_title': 'Brand Guidelines',
        'meta_description': (
            'Smart Organics brand guidelines — logo usage rules, brand colors, '
            'typography standards, and imagery guidelines for consistent brand identity.'
        ),
    }
    return render(request, 'core/brand_guidelines.html', context)


@require_POST
def newsletter_subscribe(request):
    """Handle newsletter subscription via AJAX."""
    form = NewsletterForm(request.POST)
    if form.is_valid():
        form.save()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': 'You\'ve been subscribed successfully!'
            })
        messages.success(request, 'You\'ve been subscribed successfully!')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'This email is already subscribed or invalid.'
            }, status=400)
        messages.error(request, 'This email is already subscribed or invalid.')
        return redirect(request.META.get('HTTP_REFERER', '/'))
