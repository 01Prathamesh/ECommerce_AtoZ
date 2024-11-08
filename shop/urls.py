from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import homepage, product_listing, product_detail, checkout, payment_success, payment_failure
from .views import ProductList, ProductDetail
from .views import CategoryList

urlpatterns = [
    path('', homepage, name='homepage'),
    path('products/', product_listing, name='product_listing'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('checkout/', checkout, name='checkout'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/failure/', payment_failure, name='payment_failure'),
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/categories/', CategoryList.as_view(), name='category-list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
