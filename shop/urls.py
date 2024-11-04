from django.urls import path
from .views import homepage, product_listing, product_detail, checkout, payment_success, payment_failure

urlpatterns = [
    path('', homepage, name='homepage'),
    path('products/', product_listing, name='product_listing'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('checkout/', checkout, name='checkout'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/failure/', payment_failure, name='payment_failure'),
]
