from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from unfold.admin import ModelAdmin
from solo.admin import SingletonModelAdmin
from .models import (
    SiteSettings, NavigationLink, FooterLink, CompanyValue, TeamMember,
    NewsletterSubscriber, HomePageSettings, AboutPageSettings,
    ProductsPageSettings,
    RegistrationPageSettings, WhyChooseUsItem, TradePageImage
)

@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin, ModelAdmin):
    fieldsets = (
        ('General Info', {
            'fields': ('site_name', 'tagline', 'logo', 'favicon')
        }),
        ('Contact Info', {
            'fields': ('contact_email', 'contact_phone')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'linkedin_url')
        }),
        ('Integrations', {
            'fields': ('chatbot_embed_code', 'analytics_script')
        }),
    )

@admin.register(HomePageSettings)
class HomePageSettingsAdmin(SingletonModelAdmin, ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_headline', 'hero_subtext', 'hero_background', 'hero_cta_text', 'hero_cta_link')
        }),
        ('Overview Section', {
            'fields': ('overview_badge_text', 'overview_image', 'overview_title', 'overview_tagline', 'overview_content')
        }),
        ('About Section', {
            'fields': ('about_section_badge_text', 'about_section_title', 'about_section_image', 'about_section_content')
        }),
        ('Bottom Large Image Section', {
            'fields': ('bottom_large_image',)
        }),
        ('Why Choose Us Section', {
            'fields': ('why_choose_us_headline',)
        }),
    )

@admin.register(WhyChooseUsItem)
class WhyChooseUsItemAdmin(ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title']

@admin.register(AboutPageSettings)
class AboutPageSettingsAdmin(SingletonModelAdmin, ModelAdmin):
    fieldsets = (
        ('Content Section', {
            'fields': ('mission_statement', 'vision_statement')
        }),
        ('Call to Action (CTA)', {
            'fields': ('cta_headline', 'cta_subtext', 'cta_button_text', 'cta_button_link')
        }),
    )

class TradePageImageInline(admin.TabularInline):
    model = TradePageImage
    extra = 1

@admin.register(ProductsPageSettings)
class ProductsPageSettingsAdmin(SingletonModelAdmin, ModelAdmin):
    fieldsets = (
        ('Trade Content', {
            'fields': ('trade_title', 'trade_description')
        }),
    )
    inlines = [TradePageImageInline]




@admin.register(RegistrationPageSettings)
class RegistrationPageSettingsAdmin(SingletonModelAdmin, ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_headline', 'hero_subtext', 'hero_background')
        }),
    )

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(ModelAdmin):
    list_display = ['email', 'subscribed_at']
    search_fields = ['email']

@admin.register(NavigationLink)
class NavigationLinkAdmin(ModelAdmin):
    list_display = ['label', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['label', 'url']

@admin.register(FooterLink)
class FooterLinkAdmin(ModelAdmin):
    list_display = ['label', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['label', 'url']

@admin.register(CompanyValue)
class CompanyValueAdmin(ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title']

class TeamMemberForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = TeamMember
        fields = '__all__'

@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin):
    form = TeamMemberForm
    list_display = ['name', 'role', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'role']

