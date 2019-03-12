from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from menu.models import Dish, Basket, Order


class MainView(CreateView):
    template_name = 'core/main.html'
    model = Dish
    fields = ['title', 'image', 'price', 'recipe']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Dish.objects.all().order_by('-created_date')
        return context


class CartView(CreateView):
    template_name = 'core/cart.html'
    model = Order
    fields = ['name', 'phone_number', 'location', 'delivery_date']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Basket.objects.filter(session_key=self.request.session.session_key)
        return context

    def form_valid(self, form):
        basket = Basket.objects.get(session_key=self.request.session.session_key)
        self.object = form.save(commit=False)
        self.object.basket = basket
        self.object.save()
        self.object.send_order_by_bot()
        self.request.session.flush()
        
        return super().form_valid(form)
