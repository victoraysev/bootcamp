# Generated by Django 3.2.9 on 2021-12-04 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0002_bankaccount_iban'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='customer'),
            preserve_default=False,
        ),
    ]
