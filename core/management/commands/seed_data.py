"""
Management command to seed initial data for Smart Organics website.
"""

from django.core.management.base import BaseCommand
from core.models import CompanyStats, Testimonial, FAQ, Service, Product


class Command(BaseCommand):
    help = 'Seed initial data for Smart Organics website'

    def handle(self, *args, **options):
        # ── Company Stats ──────────────────────────────
        stats_data = [
            {'label': 'Years Experience', 'value': 10, 'suffix': '+', 'icon_class': 'bi bi-calendar-check', 'order': 1},
            {'label': 'Farmers Supported', 'value': 5000, 'suffix': '+', 'icon_class': 'bi bi-people', 'order': 2},
            {'label': 'Seedlings Distributed', 'value': 500000, 'suffix': '+', 'icon_class': 'bi bi-tree', 'order': 3},
            {'label': 'Counties Reached', 'value': 47, 'suffix': '', 'icon_class': 'bi bi-geo-alt', 'order': 4},
        ]
        for s in stats_data:
            CompanyStats.objects.get_or_create(label=s['label'], defaults=s)
        self.stdout.write(self.style.SUCCESS(f'✓ {CompanyStats.objects.count()} stats loaded'))

        # ── Testimonials ───────────────────────────────
        testimonials_data = [
            {
                'farmer_name': 'James Kiprono',
                'location': 'Nandi County',
                'content': 'Since joining Smart Organics\' contract farming program, my coffee yields have increased by 40%. The certified seedlings and agronomy support have truly transformed my farm and my family\'s livelihood.',
                'is_featured': True,
            },
            {
                'farmer_name': 'Mary Wanjiku',
                'location': 'Kiambu County',
                'content': 'The organic manure from Smart Organics revived my tired soils. My crop productivity improved significantly and I no longer rely on expensive synthetic fertilizers. The results speak for themselves.',
                'is_featured': True,
            },
            {
                'farmer_name': 'Peter Ochieng',
                'location': 'Kisumu County',
                'content': 'The farmer training sessions gave me practical skills that I use every day on my farm. Smart Organics genuinely cares about farmer success and provides real knowledge that makes a difference.',
                'is_featured': True,
            },
        ]
        for t in testimonials_data:
            Testimonial.objects.get_or_create(farmer_name=t['farmer_name'], defaults=t)
        self.stdout.write(self.style.SUCCESS(f'✓ {Testimonial.objects.count()} testimonials loaded'))

        # ── FAQs ───────────────────────────────────────
        faqs_data = [
            {
                'question': 'How do I join the contract coffee farming program?',
                'answer': 'You can register for our contract farming program by contacting us via phone at 0743 581 264 or email at support@smartorganics.co.ke. We work with individual farmers and cooperatives. Our team will guide you through the registration process and explain the benefits and requirements.',
                'order': 1,
            },
            {
                'question': 'What types of coffee seedlings do you offer?',
                'answer': 'We offer certified improved coffee varieties suited to diverse agro-ecological zones across Kenya. These include disease-resistant varieties with high survival rates and superior yield potential, including Ruiru 11, Batian, and other improved varieties. Contact us for specific variety availability in your area.',
                'order': 2,
            },
            {
                'question': 'Do you deliver agricultural inputs across Kenya?',
                'answer': 'Yes, we have distribution networks across Kenya. We deliver coffee seedlings, organic manure, and other agricultural inputs to farmers in various counties. Contact us to discuss delivery options for your location and order quantities.',
                'order': 3,
            },
            {
                'question': 'How can I access your farmer training programs?',
                'answer': 'Our farmer training programs are available to all registered farmers and cooperatives. Training is conducted through demonstration farms, field visits, and workshop sessions. Register through our contact page or call us directly at 0743 581 264.',
                'order': 4,
            },
            {
                'question': 'What is Smart Organic Manure?',
                'answer': 'Smart Organic Manure is our 100% organic soil conditioner designed to improve soil fertility, enhance soil structure, and increase crop productivity. It supports sustainable agriculture by reducing dependency on synthetic inputs while improving long-term soil health.',
                'order': 5,
            },
            {
                'question': 'What areas does Smart Organics operate in?',
                'answer': 'Smart Organics is headquartered in Eldoret, Uasin Gishu County, with distribution networks and farmer programs across multiple counties in Kenya. We are expanding into regional East African markets.',
                'order': 6,
            },
        ]
        for f in faqs_data:
            FAQ.objects.get_or_create(question=f['question'], defaults=f)
        self.stdout.write(self.style.SUCCESS(f'✓ {FAQ.objects.count()} FAQs loaded'))

        # ── Services ───────────────────────────────────
        services_data = [
            {
                'name': 'Certified Coffee Seedlings',
                'slug': 'certified-coffee-seedlings',
                'short_description': 'High-quality, disease-resistant coffee seedlings suited to diverse agro-ecological zones.',
                'full_description': 'We produce and distribute certified coffee seedlings, particularly improved varieties that help farmers establish productive coffee farms capable of delivering higher yields and better market returns.',
                'icon_class': 'bi-flower2',
                'is_featured': True,
                'order': 1,
            },
            {
                'name': 'Organic Soil Nutrition',
                'slug': 'organic-soil-nutrition',
                'short_description': '100% organic soil conditioner that improves fertility and crop productivity.',
                'full_description': 'Smart Organic Manure improves soil fertility, enhances soil structure, and increases crop productivity while reducing dependency on synthetic inputs.',
                'icon_class': 'bi-droplet-half',
                'is_featured': True,
                'order': 2,
            },
            {
                'name': 'Agronomy Advisory Services',
                'slug': 'agronomy-advisory',
                'short_description': 'Professional agronomic guidance including soil management, crop husbandry, and pest control.',
                'full_description': 'Our agronomy advisory services include soil fertility management, crop husbandry guidance, pest and disease management, and farmer training programs through demonstration farms.',
                'icon_class': 'bi-people-fill',
                'is_featured': True,
                'order': 3,
            },
            {
                'name': 'Contract Coffee Farming',
                'slug': 'contract-coffee-farming',
                'short_description': 'Structured programs providing inputs, support, and market linkage.',
                'full_description': 'Our contract farming programs provide farmers with access to quality inputs, technical support, and market linkage opportunities, helping secure stable markets and improve profitability.',
                'icon_class': 'bi-handshake',
                'is_featured': True,
                'order': 4,
            },
            {
                'name': 'Farmer Training Programs',
                'slug': 'farmer-training',
                'short_description': 'Hands-on training through demonstration farms and field activities.',
                'full_description': 'Through demonstration farms and field training activities, we equip farmers with practical knowledge that improves productivity and farm management.',
                'icon_class': 'bi-mortarboard-fill',
                'is_featured': True,
                'order': 5,
            },
            {
                'name': 'Climate-Smart Agriculture',
                'slug': 'climate-smart-agriculture',
                'short_description': 'Promoting sustainable farming practices for environmental conservation.',
                'full_description': 'We promote climate-smart agricultural practices that strengthen farmer resilience, improve yields, and support environmentally responsible agriculture.',
                'icon_class': 'bi-globe-americas',
                'is_featured': True,
                'order': 6,
            },
        ]
        for s in services_data:
            Service.objects.get_or_create(slug=s['slug'], defaults=s)
        self.stdout.write(self.style.SUCCESS(f'✓ {Service.objects.count()} services loaded'))

        # ── Products ───────────────────────────────────
        products_data = [
            {
                'name': 'Certified Coffee Seedlings',
                'slug': 'certified-coffee-seedlings',
                'category': 'seedlings',
                'description': 'Improved coffee varieties suited to diverse agro-ecological zones, delivering higher yields and better market returns with disease resistance and high survival rates.',
                'features': 'Certified improved varieties,High survival rates,Disease resistant,Higher yield potential',
                'is_featured': True,
                'order': 1,
            },
            {
                'name': 'Smart Organic Manure',
                'slug': 'smart-organic-manure',
                'category': 'manure',
                'description': '100% organic soil conditioner designed to improve soil fertility, enhance soil structure, and increase crop productivity sustainably.',
                'features': '100% organic composition,Improves soil structure,Enhances water retention,Boosts crop productivity',
                'is_featured': True,
                'order': 2,
            },
            {
                'name': 'Agricultural Input Packages',
                'slug': 'agricultural-input-packages',
                'category': 'inputs',
                'description': 'Complete agricultural input packages designed for smallholder coffee farmers, including organic fertilizers, pest management solutions, and soil amendments.',
                'features': 'Complete farm input sets,Organic solutions,Expert recommendations,Affordable pricing',
                'is_featured': True,
                'order': 3,
            },
        ]
        for p in products_data:
            Product.objects.get_or_create(slug=p['slug'], defaults=p)
        self.stdout.write(self.style.SUCCESS(f'✓ {Product.objects.count()} products loaded'))

        self.stdout.write(self.style.SUCCESS('\n✅ All seed data loaded successfully!'))
