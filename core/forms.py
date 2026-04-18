"""
Forms for Smart Organics website.
"""

from django import forms
from .models import ContactMessage, Newsletter


class ContactForm(forms.ModelForm):
    """Contact form with Bootstrap-styled widgets."""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'id': 'contact-name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com',
                'id': 'contact-email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+254 7XX XXX XXX',
                'id': 'contact-phone',
            }),
            'subject': forms.Select(attrs={
                'class': 'form-select',
                'id': 'contact-subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us how we can help you...',
                'rows': 5,
                'id': 'contact-message',
            }),
        }


class NewsletterForm(forms.ModelForm):
    """Newsletter subscription form."""
    
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'id': 'newsletter-email',
            }),
        }
