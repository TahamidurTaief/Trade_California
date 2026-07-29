from .models import (
    SiteSettings, NavigationLink, FooterLink,
    HomePageSettings, AboutPageSettings, ProductsPageSettings,
    ContactPageSettings, RegistrationPageSettings
)

def site_context(request):
    try:
        settings = SiteSettings.objects.get()
    except SiteSettings.DoesNotExist:
        settings = None

    try:
        home_settings = HomePageSettings.objects.get()
    except HomePageSettings.DoesNotExist:
        home_settings = None

    try:
        about_settings = AboutPageSettings.objects.get()
    except AboutPageSettings.DoesNotExist:
        about_settings = None

    try:
        products_settings = ProductsPageSettings.objects.get()
    except ProductsPageSettings.DoesNotExist:
        products_settings = None

    try:
        contact_settings = ContactPageSettings.objects.get()
    except ContactPageSettings.DoesNotExist:
        contact_settings = None
        
    try:
        registration_settings = RegistrationPageSettings.objects.get()
    except RegistrationPageSettings.DoesNotExist:
        registration_settings = None

    nav_links = NavigationLink.objects.filter(is_active=True)
    footer_links = FooterLink.objects.filter(is_active=True)

    return {
        'site_settings': settings,
        'home_settings': home_settings,
        'about_settings': about_settings,
        'products_settings': products_settings,

        'contact_settings': contact_settings,
        'registration_settings': registration_settings,
        'nav_links': nav_links,
        'footer_links': footer_links,
    }
