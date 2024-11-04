from django.shortcuts import render
from .models import Product

def homepage(request):
    # Retrieve featured products
    featured_products = Product.objects.filter(is_active=True, is_featured=True)

    context = {
        'featured_products': featured_products
    }
    return render(request, 'homepage.html', context)
