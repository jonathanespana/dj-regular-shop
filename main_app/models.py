from django.contrib.postgres.fields import ArrayField

from django.db import models

# Create your models here.

CATEGORIES=(
    ('G', 'Genderless'),
    ('M', 'Men'),
    ('W', 'Women'),
    ('A', 'Accessories'),
)

SUBCATEGORIES=(
    ('T', 'Tops'),
    ('B', 'Bottoms'),
    ('H', 'Headware'),
    ('A', 'Accessories'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=100, default="Add Product Name")
    product_description = models.CharField(max_length=500, default="Add Product Description")
    product_fabrics = models.CharField(max_length=300, default="4way Stretch Recycle Polyester 3L")
    category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
    subcategory = models.CharField(max_length=1, choices=SUBCATEGORIES, default=SUBCATEGORIES[0][0])
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    xs = models.IntegerField(default=0)
    s = models.IntegerField(default=0)
    m = models.IntegerField(default=0)
    l = models.IntegerField(default=0)
    xl = models.IntegerField(default=0)
    xxl = models.IntegerField(default=0)
    fits_all = models.IntegerField(default=0)

    
    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    image_name = models.CharField(max_length= 150)
    image_url = models.URLField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)