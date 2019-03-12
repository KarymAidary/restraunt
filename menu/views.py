from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Dish, Basket, BasketItem
from .forms import DishForm
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string


class DishUpdateView(UpdateView):
    model = Dish
    fields = ['title', 'image', 'price', 'recipe']
    template_name = 'menu/detail_update_dish.html'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Dish, id=id)


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    print(data.get("dish_id"))
    dish = Dish.objects.filter(id=data.get("dish_id")).first()
    amount = data.get("dish_amount")
    new_basket, created = Basket.objects.get_or_create(session_key=session_key)
    basket_item, created = BasketItem.objects.get_or_create(dish=dish,
                                                            defaults={"amount": amount}
                                                            )
    if not created:
        basket_item.amount += int(amount)
        basket_item.save(force_update=True)

    new_basket.dishes.add(basket_item)
    new_basket.count_total_price()
    dish_total = new_basket.dishes.count()
    return_dict["dish_total"] = dish_total
    return JsonResponse(return_dict)


def remove_from_basket(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    dishes_id = data.get("remove_item_id")
    if dishes_id:
        basket = Basket.objects.get(session_key=session_key)
        basket.dishes.get(id=dishes_id).delete()
        return_dict["is_deleted"] = True
        return_dict['dishes_total'] = basket.dishes.count()
        if basket.dishes.count() < 1 or basket.total <= 3.50:
            basket.delete()
            return_dict['empty_basket'] = render_to_string('core/empty_basket.html')
        else:
            basket.count_total_price()
        return_dict['basket_total'] = basket.total
    return JsonResponse(return_dict)
