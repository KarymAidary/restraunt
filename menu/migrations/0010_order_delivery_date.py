# Generated by Django 2.1.7 on 2019-03-12 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20190312_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
