from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product, Category
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'parent', 'order']
    list_editable = ['order']
    search_fields = ['name']
    list_filter = ['parent']

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['image_preview', 'category', 'is_featured', 'order']
    list_display_links = ['image_preview']
    list_editable = ['category', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"
