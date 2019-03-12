# Generated by Django 2.1.7 on 2019-03-10 22:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_menu_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='total')),
                ('session_key', models.CharField(default=None, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='Amount')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='Dish',
        ),
        migrations.AddField(
            model_name='basketitem',
            name='dish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Dish'),
        ),
        migrations.AddField(
            model_name='basket',
            name='dishes',
            field=models.ManyToManyField(to='menu.BasketItem'),
        ),
    ]
