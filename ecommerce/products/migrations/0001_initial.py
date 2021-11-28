# Generated by Django 3.2.9 on 2021-11-28 10:29

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
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('sku', models.CharField(max_length=100, unique=True, verbose_name='SKU')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(max_length=2000, verbose_name='Description')),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('white', 'White'), ('yellow', 'Yellow')], max_length=20, verbose_name='Color')),
                ('size', models.CharField(max_length=30, verbose_name='Size')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]