
from django.db import models

# Create your models here.

CATEGORIES=(
    ('Genderless', 'Genderless'),
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Accessories', 'Accessories'),
)

SUBCATEGORIES=(
    ('Tops', 'Tops'),
    ('Bottoms', 'Bottoms'),
    ('Headware', 'Headware'),
    ('Accessories', 'Accessories'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=100, default="Add Product Name")
    product_description = models.CharField(max_length=500, default="Add Product Description")
    product_fabrics = models.CharField(max_length=300, default="4way Stretch Recycle Polyester 3L")
    category = models.CharField(choices=CATEGORIES, default=CATEGORIES[0][0])
    subcategory = models.CharField(choices=SUBCATEGORIES, default=SUBCATEGORIES[0][0])
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    xs = models.IntegerField(default=0)
    s = models.IntegerField(default=0)
    m = models.IntegerField(default=0)
    l = models.IntegerField(default=0)
    xl = models.IntegerField(default=0)
    xxl = models.IntegerField(default=0)
    fits_all = models.IntegerField(default=0)
    slug_name = models.SlugField(default="", null=False)
    slug_category = models.SlugField(default="", null=False)
    slug_subcategory = models.SlugField(default="", null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    
    def __str__(self):
        return self.product_name
    
    @property
    def main_image(self):
        product_image = self.productimage_set.all()
        main_image = product_image[0]
        return main_image



class ProductImage(models.Model):
    image_name = models.CharField(max_length= 250)
    image_url = models.URLField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Photo for Product:{self.product.product_name} @{self.image_url}"


class ProductPrice(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    description = models.CharField(max_length=200, default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.product_name} {self.price}"
    

class Cart(models.Model):
    session_id = models.CharField(max_length=100, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.session_id
    
    @property
    def total_price(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.price for item in cartitems])
        return total
    
    @property
    def num_of_items(self):
        cartitems = self.cartitem_set.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    
    @property
    def all_items(self):
        cartitems = self.cartitem_set.all()
        return cartitems
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    size_choice = models.CharField(max_length=10, default="")
    color_choice = models.CharField(max_length=20, default="")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.product_name
    
    @property
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price
    

""" ***** Create Order ****** """
""" *** takes in a completed cart, customer info to update and send product: full name, address, shipping method, phone number, email address *** """

