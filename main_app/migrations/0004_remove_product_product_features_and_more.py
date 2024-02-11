# Generated by Django 5.0.1 on 2024-02-11 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_features',
        ),
        migrations.AddField(
            model_name='product',
            name='product_fabrics',
            field=models.CharField(default='4way Stretch Recycle Polyester 3L', max_length=300),
        ),
    ]