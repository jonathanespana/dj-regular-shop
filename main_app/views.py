from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main_app/home.html')

def category(request):
    return render(request, 'main_app/shop-category.html')

def product_detail(request):
    return render(request, 'main_app/product-detail.html')