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

def product_detail(request, product_id):
    # Retrieve the specific product
    product = Product.objects.get(id=product_id)

    context = {
        'product': product,
        'current_year': datetime.now().year,
    }
    return render(request, 'pdp.html', context)

def checkout(request):
    if request.method == 'POST':
        # Handle form submission and process order here
        # For simplicity, we assume the order is always successful
        return render(request, 'mpp.html', {'current_year': datetime.now().year})

    return render(request, 'cop.html', {'current_year': datetime.now().year})
