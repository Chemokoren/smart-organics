"""
Admin configuration for Smart Organics core models.
"""

from django.contrib import admin
from .models import (
    ContactMessage, TeamMember, Testimonial, 
    Product, Service, FAQ, CompanyStats, Newsletter
)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('subject', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'role')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'location', 'is_featured', 'created_at')
    list_filter = ('is_featured',)
    list_editable = ('is_featured',)
    search_fields = ('farmer_name', 'location', 'content')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'order')
    list_filter = ('category', 'is_featured')
    list_editable = ('is_featured', 'order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'order')
    list_filter = ('is_featured',)
    list_editable = ('is_featured', 'order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'short_description')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_published')
    list_filter = ('is_published',)
    list_editable = ('order', 'is_published')


@admin.register(CompanyStats)
class CompanyStatsAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'suffix', 'order')
    list_editable = ('value', 'suffix', 'order')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email',)
