# Generated by Django 5.0.1 on 2024-02-19 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Add Product Name', max_length=100)),
                ('product_description', models.CharField(default='Add Product Description', max_length=500)),
                ('product_fabrics', models.CharField(default='4way Stretch Recycle Polyester 3L', max_length=300)),
                ('category', models.CharField(choices=[('G', 'Genderless'), ('M', 'Men'), ('W', 'Women'), ('A', 'Accessories')], default='G', max_length=1)),
                ('subcategory', models.CharField(choices=[('T', 'Tops'), ('B', 'Bottoms'), ('H', 'Headware'), ('A', 'Accessories')], default='T', max_length=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('xs', models.IntegerField(default=0)),
                ('s', models.IntegerField(default=0)),
                ('m', models.IntegerField(default=0)),
                ('l', models.IntegerField(default=0)),
                ('xl', models.IntegerField(default=0)),
                ('xxl', models.IntegerField(default=0)),
                ('fits_all', models.IntegerField(default=0)),
                ('slug', models.SlugField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=150)),
                ('image_url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product')),
            ],
        ),
    ]
