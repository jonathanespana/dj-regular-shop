from django.http import Http404
from django.shortcuts import render

from .models import Product

# Create your views here.

def home(request):
    return render(request, 'main_app/home.html')

def category(request):
    products = Product.objects.all()
    context = { 'products': products}
    return render(request, 'main_app/shop-category.html', context)

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        context = { 'product': product}
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'main_app/product-detail.html' , context)

def cart(request):
    return render(request, 'main_app/my-cart.html')

def team(request):
    return render(request, 'main_app/team.html')

def team_member(request):
    return render(request, 'main_app/team-member.html')

def checkout(request):
    return render(request, 'main_app/checkout.html')