import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from apps.core.models import (
    HomePageSettings, AboutPageSettings, ProductsPageSettings,
    ServicesPageSettings, ContactPageSettings, RegistrationPageSettings
)
from django.core.files import File

def seed():
    print("Seeding Page Settings...")

    # Home Page
    home, _ = HomePageSettings.objects.get_or_create()
    home.hero_headline = "Expand Your Global Reach"
    home.hero_subtext = "Premium Trade & International Business Platform"

    home.hero_cta_text = "Register Now"
    home.hero_cta_link = "/registration/"
    if os.path.exists('media/site/hero/hero_home.png'):
        home.hero_background = 'site/hero/hero_home.png'
    home.save()

    # About Page
    about, _ = AboutPageSettings.objects.get_or_create()
    about.hero_headline = "About Trade California"
    about.hero_subtext = "Your trusted partner in international commerce."

    if os.path.exists('media/site/hero/hero_about.png'):
        about.hero_background = 'site/hero/hero_about.png'
    about.save()

    # Products Page
    products, _ = ProductsPageSettings.objects.get_or_create()
    products.hero_headline = "Trade Catalog"
    products.hero_subtext = "Explore our premium selection of export-ready products sourced from verified suppliers."

    if os.path.exists('media/site/hero/hero_home.png'):
        products.hero_background = 'site/hero/hero_home.png' # Reusing home image for demo
    products.save()

    # Services Page
    services, _ = ServicesPageSettings.objects.get_or_create()
    services.hero_headline = "Our Services"
    services.hero_subtext = "Comprehensive international trade solutions tailored to your business role."

    if os.path.exists('media/site/hero/hero_about.png'):
        services.hero_background = 'site/hero/hero_about.png' # Reusing about image for demo
    services.save()

    # Contact Page
    contact, _ = ContactPageSettings.objects.get_or_create()
    contact.hero_headline = "Contact Us"
    contact.hero_subtext = "Get in touch with our team of global trade experts."

    if os.path.exists('media/site/hero/hero_home.png'):
        contact.hero_background = 'site/hero/hero_home.png'
    contact.save()

    # Registration Page
    reg, _ = RegistrationPageSettings.objects.get_or_create()
    reg.hero_headline = "Partner Registration"
    reg.hero_subtext = "Join our exclusive network of premium buyers, sellers, and distributors."

    if os.path.exists('media/site/hero/hero_about.png'):
        reg.hero_background = 'site/hero/hero_about.png'
    reg.save()

    print("Seeding complete!")

if __name__ == '__main__':
    seed()
