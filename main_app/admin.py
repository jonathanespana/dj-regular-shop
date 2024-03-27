from django.contrib import admin

from .models import Product, ProductImage, ProductPrice, Cart, CartItem

class ProductPriceAdmin(admin.StackedInline):
    model = ProductPrice

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product Information', {'fields': ['product_name', 'price', 'product_description', 'product_fabrics']}),
        ('Product Categories', {'fields': ['category', 'subcategory']}),
        ('Product Inventory', {'fields': ['xs', 's', 'm', 'l', 'xl', 'xxl', 'fits_all']}),
        ('Product Slugs', {'fields': ['slug_name', 'slug_category', 'slug_subcategory']}),
    ]
    prepopulated_fields = {
        "slug_name": ["product_name"], 
        "slug_category": ["category"],
        "slug_subcategory": ["subcategory"],
        }

    list_display = ['product_name', 'product_description', 'product_fabrics', 'category', 'subcategory']
    inlines = [ProductPriceAdmin, ProductImageInline]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductPrice)
admin.site.register(Cart)
admin.site.register(CartItem)