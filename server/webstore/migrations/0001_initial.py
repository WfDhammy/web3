# Generated by Django 5.1.5 on 2025-01-22 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225, unique=True)),
                ('image', models.ImageField(upload_to='brand_images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageFiled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('display_image', models.ImageField(upload_to='product_display_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstore.category')),
                ('images', models.ManyToManyField(to='webstore.imagefiled')),
            ],
            options={
                'ordering': ['uploaded_at'],
            },
        ),
    ]
