from decimal import Decimal
from django.urls import reverse
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.template.loader import render_to_string
import requests


class Dish(models.Model):
    title = models.CharField(verbose_name="Название блюда", max_length=100, null=True, default=None)
    image = models.ImageField(verbose_name="Картинка", upload_to="menu", null=True, default="")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    recipe = models.TextField(verbose_name="Краткий рецепт", )


    def __str__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        return reverse("menu:menu_detail", kwargs={"pk": self.pk})


class BasketItem(models.Model):
    dish = models.ForeignKey(to='Dish', null=True, on_delete=models.CASCADE, unique=False)
    amount = models.PositiveIntegerField(default=1)
    add_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s' % self.dish


class Basket(models.Model):
    total = models.DecimalField(verbose_name='total', max_digits=10, decimal_places=2, default=0)
    session_key = models.CharField(max_length=128, default=None)
    dishes = models.ManyToManyField(to='BasketItem')

    def count_total_price(self):
        items = self.dishes.all()
        total = 0
        for item in items:
            total += item.dish.price * item.amount
        self.total = Decimal(total)
        self.save()

    def __str__(self):
        return '%s' % self.id


class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200, null=True, default=None)
    phone_number = PhoneNumberField(verbose_name='Мобильный телефон', default=None)
    delivery_date = models.DateTimeField(verbose_name="Время (дата) доставки", default=timezone.now)
    location = models.CharField(verbose_name="Адресс Доставки (киоск)", max_length=225, null=True, default=None)
    date_ordered = models.DateTimeField(auto_now=True)
    basket = models.OneToOneField('Basket', on_delete=models.CASCADE, related_name='basket', default=None)
    sent_by_bot = models.BooleanField(default=False)


    def send_order_by_bot(self):
        context = {
            "order_id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "delivery_date": self.delivery_date,
            "location": self.location,
            "date_ordered": self.date_ordered,
            "items": self.basket.dishes.all(),
        }
        message = render_to_string('messages/message.txt', context)
        bot_token = '782909773:AAEnUd0rbfXEGQEc8hD3QFsBVdOSHH62ehA'
        bot_chatID = '131660854'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message

        response = requests.get(send_text)

        return response.json()