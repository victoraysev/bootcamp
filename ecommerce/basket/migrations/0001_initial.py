# Generated by Django 3.2.9 on 2021-12-02 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('status', models.CharField(choices=[('open', 'Open'), ('submitted', 'Submitted'), ('merged', 'Merged')], default=0, max_length=20, verbose_name='Status Type')),
            ],
            options={
                'verbose_name': 'basket',
                'verbose_name_plural': 'baskets',
            },
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket', verbose_name='basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'basket item',
                'verbose_name_plural': 'basket items',
                'db_table': 'basket_basket_item',
            },
        ),
    ]