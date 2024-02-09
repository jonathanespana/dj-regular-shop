from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/category/', views.category, name='category'),
    path('shop/category/product-name', views.product_detail, name='product_detail'),
    path('cart', views.cart, name='cart'),
]