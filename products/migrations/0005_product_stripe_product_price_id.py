# Generated by Django 4.2.16 on 2024-10-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_auto_20240930_1418"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stripe_product_price_id",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
