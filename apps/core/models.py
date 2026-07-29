from django.db import models
from solo.models import SingletonModel
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

class SiteSettings(SingletonModel):
    site_name = models.CharField(max_length=255, default="Trade California International")
    tagline = models.CharField(max_length=255, default="Connecting American Products with International Markets")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Contact Info
    contact_email = models.EmailField(blank=True, default="contact@tradecalifornia.com")
    contact_phone = models.CharField(max_length=50, blank=True, default="+1 (800) 123-4567")
    
    # Social Media Links
    facebook_url = models.URLField(blank=True, default="https://facebook.com")
    twitter_url = models.URLField(blank=True, default="https://twitter.com")
    linkedin_url = models.URLField(blank=True, default="https://linkedin.com")
    
    # External integrations
    chatbot_embed_code = models.TextField(blank=True, help_text="Paste your Tawk.to or other chatbot script here")
    analytics_script = models.TextField(blank=True, help_text="Google Analytics or similar")

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

class CompanyValue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Heroicons icon name, e.g. 'GlobeAltIcon'", blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = RichTextField()
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class NavigationLink(models.Model):
    label = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

class FooterLink(models.Model):
    label = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# --- Page Settings Models ---

class HomePageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Expand Your Global Reach", blank=True, null=True)
    hero_subtext = models.TextField(default="Premium Trade & International Business Platform", blank=True, null=True)
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)

    hero_cta_text = models.CharField(max_length=50, default="Register Now", blank=True)
    hero_cta_link = models.CharField(max_length=255, default="/registration/", blank=True)
    
    why_choose_us_badge_text = models.CharField(max_length=50, default="Why Us", blank=True)
    why_choose_us_headline = models.CharField(max_length=255, default="Why Trade California?")
    
    # Overview Section
    overview_badge_text = models.CharField(max_length=50, default="Overview", blank=True)
    overview_image = models.ImageField(upload_to='site/overview/', blank=True, null=True)
    overview_title = models.CharField(max_length=255, default="Connecting American Opportunity with Global Markets.", blank=True)
    overview_tagline = models.CharField(max_length=255, default="From California to the World.", blank=True)
    overview_content = HTMLField(blank=True, default="<p>Founded by <strong>Andrew Hughan</strong>, former USAIF professional, <span class=\"font-medium\">Trade California</span> is a Sacramento, California-based international trade and business development platform operated by <strong>American Green Technology, LLC.</strong></p><p>Trade California connects global buyers, distributors, governments, and business partners with trusted U.S.-based products, commodities, services, and business opportunities—helping build meaningful connections between American businesses and international markets.</p>")

    # About Section (Right above Why Choose Us)
    about_section_badge_text = models.CharField(max_length=50, default="About Us", blank=True)
    about_section_title = models.CharField(max_length=255, default="About Trade California", blank=True)
    about_section_image = models.ImageField(upload_to='site/about/', blank=True, null=True)
    
    # Bottom Large Image Section
    bottom_large_image = models.ImageField(upload_to='site/bottom_banner/', blank=True, null=True, help_text="Large image displayed at the bottom of the home page")
    
    about_section_content = HTMLField(blank=True, default="""
    <h3 style="font-weight: bold; font-size: 1.125rem; margin-bottom: 0.5rem;">Your Gateway to U.S. Trade</h3>
    <p style="margin-bottom: 1rem;">Trade California supports international businesses, government buyers, distributors, and organizations seeking reliable access to American products and business opportunities.</p>
    <p style="margin-bottom: 1.5rem;">Our focus is to connect qualified international buyers with U.S.-based suppliers while providing support across sourcing, communication, logistics coordination, product consultancy, and international business development.</p>
    
    <h3 style="font-weight: bold; font-size: 1.125rem; margin-bottom: 0.5rem;">Our Core Areas</h3>
    <ul style="list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem;">
        <li>U.S. Commodity Trading</li>
        <li>Agriculture & Food Trading</li>
        <li>Healthcare Products</li>
    </ul>
    <ul style="list-style-type: disc; padding-left: 1.5rem; font-weight: bold; margin-bottom: 1rem;">
        <li>Energy Commodities</li>
    </ul>
    <ul style="list-style-type: disc; padding-left: 1.5rem; font-weight: bold; margin-bottom: 1rem;">
        <li>Industrial Commodities</li>
    </ul>
    <ul style="list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem;">
        <li style="font-weight: bold;">Consumer & Lifestyle Products</li>
        <li>International Business Consultancy</li>
        <li>U.S. Product Consultancy</li>
        <li>Logistics Support</li>
        <li>Contract & Trade Facilitation</li>
    </ul>
    """)

    def __str__(self):
        return "Home Page Settings"
    
    class Meta:
        verbose_name = "Home Page Settings"
        verbose_name_plural = "Home Page Settings"

class WhyChooseUsItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class AboutPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="About Us", blank=True, null=True)
    hero_subtext = models.TextField(default="Trade California International", blank=True, null=True)
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)

    
    mission_statement = models.TextField(blank=True, default="To connect American businesses with global opportunities.")
    vision_statement = models.TextField(blank=True, default="Empowering trade without borders.")
    
    cta_headline = models.CharField(max_length=255, default="Ready to Partner With Us?")
    cta_subtext = models.TextField(default="Join thousands of verified businesses expanding their global footprint through Trade California International.", blank=True)
    cta_button_text = models.CharField(max_length=50, default="Apply to Partner Program")
    cta_button_link = models.CharField(max_length=255, default="/registration/")

    def __str__(self):
        return "About Page Settings"
    
    class Meta:
        verbose_name = "About Page Settings"
        verbose_name_plural = "About Page Settings"

class ProductsPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Our Products", blank=True, null=True)
    hero_subtext = models.TextField(default="Explore our premium catalog of American products.", blank=True, null=True)
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)

    catalog_badge_text = models.CharField(max_length=50, default="Global Export Portfolio", blank=True)
    catalog_title_prefix = models.CharField(max_length=100, default="California's Premium", blank=True)
    catalog_title_highlight = models.CharField(max_length=100, default="Trade Directory", blank=True)
    catalog_subtext = models.TextField(default="Seamlessly navigate our meticulously curated selection of high-value commodities, agricultural products, and industrial resources ready for the global market.", blank=True)


    def __str__(self):
        return "Products Page Settings"
    
    class Meta:
        verbose_name = "Products Page Settings"
        verbose_name_plural = "Products Page Settings"



class ContactPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Contact Us", blank=True, null=True)
    hero_subtext = models.TextField(default="Get in touch with our expert team today.", blank=True, null=True)
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)


    def __str__(self):
        return "Contact Page Settings"
    
    class Meta:
        verbose_name = "Contact Page Settings"
        verbose_name_plural = "Contact Page Settings"

class RegistrationPageSettings(SingletonModel):
    hero_headline = models.CharField(max_length=255, default="Partner Registration", blank=True, null=True)
    hero_subtext = models.TextField(default="Join our global network of verified trade partners.", blank=True, null=True)
    hero_background = models.ImageField(upload_to='site/hero/', blank=True, null=True)


    def __str__(self):
        return "Registration Page Settings"
    
    class Meta:
        verbose_name = "Registration Page Settings"
        verbose_name_plural = "Registration Page Settings"
