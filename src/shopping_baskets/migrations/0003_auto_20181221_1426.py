# Generated by Django 2.1.4 on 2018-12-21 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_baskets', '0002_auto_20181221_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingbasket',
            name='product',
            field=models.ManyToManyField(related_name='shopping_basket_products', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='shoppingbasket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
