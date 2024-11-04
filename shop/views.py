import datetime
from django.shortcuts import render
from .models import Product

def homepage(request):
    # Retrieve featured products
    featured_products = Product.objects.filter(is_active=True, is_featured=True)

    context = {
        'featured_products': featured_products
    }
    return render(request, 'homepage.html', context)

def product_listing(request):
    # Retrieve all products
    products = Product.objects.filter(is_active=True)

    context = {
        'products': products,
        'current_year': datetime.now().year,
    }
    return render(request, 'plp.html', context)
