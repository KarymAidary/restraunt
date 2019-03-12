from django.contrib import admin
from .models import Dish, Basket, BasketItem, Order
# Register your models here.
admin.site.register(Dish)
admin.site.register(BasketItem)
admin.site.register(Basket)
admin.site.register(Order)