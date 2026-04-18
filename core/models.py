"""
Core models for Smart Organics website.
"""

from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    """Stores contact form submissions from website visitors."""
    
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('seedlings', 'Coffee Seedlings'),
        ('inputs', 'Organic Inputs'),
        ('contract', 'Contract Farming'),
        ('training', 'Farmer Training'),
        ('partnership', 'Partnership Inquiry'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=30, choices=SUBJECT_CHOICES, default='general')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} — {self.get_subject_display()} ({self.created_at.strftime('%Y-%m-%d')})"


class TeamMember(models.Model):
    """Company team member profiles."""
    
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return f"{self.name} — {self.role}"


class Testimonial(models.Model):
    """Farmer testimonials and success stories."""
    
    farmer_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-is_featured', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return f"{self.farmer_name} — {self.location}"


class Product(models.Model):
    """Products offered by Smart Organics."""
    
    CATEGORY_CHOICES = [
        ('seedlings', 'Coffee Seedlings'),
        ('inputs', 'Organic Inputs'),
        ('manure', 'Organic Manure'),
    ]
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    features = models.TextField(blank=True, help_text='Comma-separated list of features')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
    
    def get_features_list(self):
        """Return features as a list."""
        if self.features:
            return [f.strip() for f in self.features.split(',') if f.strip()]
        return []


class Service(models.Model):
    """Services offered by Smart Organics."""
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    icon_class = models.CharField(
        max_length=50, 
        default='bi-leaf',
        help_text='Bootstrap icon class (e.g., bi-leaf, bi-water, bi-people)'
    )
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.name


class FAQ(models.Model):
    """Frequently asked questions."""
    
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
    
    def __str__(self):
        return self.question


class CompanyStats(models.Model):
    """Company statistics for display on the website."""
    
    label = models.CharField(max_length=100)
    value = models.PositiveIntegerField()
    suffix = models.CharField(max_length=10, blank=True, help_text='e.g., +, K, %')
    icon_class = models.CharField(max_length=50, default='bi-bar-chart')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Company Stat'
        verbose_name_plural = 'Company Stats'
    
    def __str__(self):
        return f"{self.label}: {self.value}{self.suffix}"


class Newsletter(models.Model):
    """Newsletter subscription emails."""
    
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'
    
    def __str__(self):
        return self.email
