# Generated by Django 5.1.5 on 2025-01-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0003_rename_product_items_cart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
