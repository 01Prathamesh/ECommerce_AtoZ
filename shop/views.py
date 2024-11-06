from datetime import datetime 
from django.shortcuts import render, redirect
from .models import Product, Order
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer

def homepage(request):
    # Retrieve featured products and categories
    featured_products = Product.objects.filter(is_active=True, is_featured=True)
    categories = Category.objects.all()

    context = {
        'featured_products': featured_products,
        'categories': categories,
        'current_year': datetime.now().year
    }
    return render(request, 'homepage.html', context)


def product_listing(request):
    # Retrieve products based on category filter or search query
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search')

    products = Product.objects.filter(is_active=True)

    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    if search_query:
        products = products.filter(name__icontains=search_query)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
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
        # Handle form submission and process order
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        product_id = request.POST.get('product_id')  # Assuming you pass the product ID from the form
        quantity = request.POST.get('quantity', 1)  # Default to 1 if not specified

        try:
            product = Product.objects.get(id=product_id)
            if product.is_in_stock() and product.stock >= int(quantity):
                # Create an order
                order = Order(product=product, quantity=int(quantity))
                order.save()

                # Update product stock
                product.stock -= int(quantity)
                product.save()

                # Redirect to payment success page
                return redirect('payment_success')  # Ensure this URL name matches your urls.py

            else:
                return redirect('payment_failure')  # Redirect to failure page if stock is insufficient

        except Product.DoesNotExist:
            return redirect('payment_failure')  # Redirect to failure page if product does not exist

    # Render the checkout form on GET requests
    return render(request, 'cop.html', {'current_year': datetime.now().year})


def payment_success(request):
    return render(request, 'mpsp.html', {'current_year': datetime.now().year})

def payment_failure(request):
    return render(request, 'mpfp.html', {'current_year': datetime.now().year})

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
