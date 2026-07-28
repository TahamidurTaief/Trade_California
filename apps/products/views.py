from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    total_products_count = products.count()
    main_categories = Category.objects.filter(parent__isnull=True).prefetch_related('children__children')
    
    return render(request, "products/list.html", {
        "products": products, 
        "total_products_count": total_products_count,
        "main_categories": main_categories
    })
