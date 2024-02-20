from django.http import Http404
from django.shortcuts import render, redirect

import uuid
import boto3
from botocore.exceptions import ClientError

from .models import Product, ProductImage

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'regularshop'

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

def add_photo(request, product_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo_name = photo_file.name
            # we can assign to cat_id or cat (if you have a cat object)
            photo = ProductImage(image_name=photo_name, image_url=url, product_id=product_id)
            photo.save()
        except ClientError as e:
            print(e)
    return redirect('product_detail', product_id=product_id)


def cart(request):
    return render(request, 'main_app/my-cart.html')

def team(request):
    return render(request, 'main_app/team.html')

def team_member(request):
    return render(request, 'main_app/team-member.html')

def checkout(request):
    return render(request, 'main_app/checkout.html')