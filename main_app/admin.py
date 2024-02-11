from django.contrib import admin

from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product Information', {'fields': ['product_name', 'price', 'product_description', 'product_fabrics']}),
        ('Product Categories', {'fields': ['category', 'subcategory']}),
        ('Product Inventory', {'fields': ['xs', 's', 'm', 'l', 'xl', 'xxl', 'fits_all']}),
    ]

    list_display = ['product_name', 'product_description', 'product_fabrics', 'category', 'subcategory']
    inlines = [ProductImageInline]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)