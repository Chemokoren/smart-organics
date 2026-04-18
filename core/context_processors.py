"""
Context processors for Smart Organics website.
Provides global template context data.
"""

from .forms import NewsletterForm


def site_context(request):
    """Inject site-wide context variables into every template."""
    return {
        'company_name': 'Smart Organics Limited',
        'company_short': 'Smart Organics',
        'company_tagline': 'Healthy Soil • Wealthy Farmers • Better Life',
        'company_phone': '0743 581 264',
        'company_phone_alt': '0755 555 140',
        'company_email': 'support@smartorganics.co.ke',
        'company_location': 'Eldoret, Uasin Gishu County, Kenya',
        'company_year': 2015,
        'social_instagram': 'https://instagram.com/smartorganics',
        'social_facebook': 'https://facebook.com/smartorganics',
        'social_twitter': 'https://twitter.com/smartorganics',
        'social_linkedin': 'https://linkedin.com/company/smartorganics',
        'newsletter_form': NewsletterForm(),
    }
