# Generated by Django 3.2.13 on 2024-09-30 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
