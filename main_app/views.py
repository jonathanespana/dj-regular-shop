from django.http import Http404
from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView

import stripe
import uuid
import boto3
from botocore.exceptions import ClientError

from .models import Product, ProductImage, Cart, CartItem
from .forms import AddToCartForm

stripe.api_key = settings.STRIPE_SECRET_KEY

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'regularshop'

# Create your views here.

def home(request):
    return render(request, 'main_app/home.html')

def category(request, slug_category, slug_subcategory):
    try:
        products = Product.objects.filter(slug_category=slug_category, slug_subcategory=slug_subcategory)
        context = { 'products': products, 'slug_category': slug_category, 'slug_subcategory': slug_subcategory}
    except Product.DoesNotExist:
        raise Http404("Product does not exists")
    return render(request, 'main_app/shop-category.html', context)

def product_detail(request, slug_name):
    form = AddToCartForm()
    try:
        product = Product.objects.get(slug_name=slug_name)
        context = { 'product': product, 'form': form}
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

def add_to_cart(request, product_id):
    if request.method == "POST":
        product = Product.objects.get(id = product_id)
        form = AddToCartForm(request.POST)

        if form.is_valid():
            size_choice = form.cleaned_data["size_choice"]
            color_choice = form.cleaned_data["color_choice"]
            quantity = form.cleaned_data["quantity"]

            if request.session.get("nonuser"):
                cart = Cart.objects.get(session_id = request.session['nonuser'], completed=False)
                cartitem, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id, quantity=quantity, size_choice=size_choice, color_choice=color_choice)
                cartitem.save()
                num_of_item = cart.num_of_items

            else:
                request.session['nonuser'] = str(uuid.uuid4())
                cart = Cart.objects.create(session_id = request.session['nonuser'], completed=False)
                cartitem, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id, quantity=quantity, size_choice=size_choice, color_choice=color_choice)
                cartitem.save()
                num_of_item = cart.num_of_items

                print(cartitem)
    else:
        form = AddToCartForm()

    return redirect('product_detail', slug_name=product.slug_name)

class CreateStripeCheckoutSessionView(View):
    """ Create Stripe checkout session """
    def post(self, request, cart_id, *args, **kwargs):
        cart = Cart.objects.get( id=cart_id, completed=False)
        cart_price = cart.total_price
        cart_items = cart.all_items 
        cart_lines = []
        for items in cart_items:
            cart_item = {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(items.product.price) * 100,
                    "product_data": {
                        "name": items.product.product_name,
                        "images": [items.product.main_image.image_url],
                    } 
                },
            "quantity": items.quantity,
            }
            cart_lines.append(cart_item)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items = cart_lines,
            metadata={"cart_id": cart.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)

class SuccessView(TemplateView):
    template_name = "main_app/success.html"

class CancelView(TemplateView):
    template_name = "main_app/cancel.html"

def team(request):
    team_avatars = ['https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar1.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar2.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar3.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar4.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar5.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar6.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar7.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar8.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar9.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar10.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar11.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar12.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar13.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar14.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar15.png',
                    'https://regularshop.s3.us-west-1.amazonaws.com/team-avatars/avatar16.png',
                    ]
    context = { 'team_avatars': team_avatars}

    return render(request, 'main_app/team.html', context)

def team_member(request):
    return render(request, 'main_app/team-member.html')

def checkout(request):
    return render(request, 'main_app/checkout.html')