# Generated by Django 2.1.7 on 2019-03-12 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_order_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время (дата) доставки'),
        ),
    ]
