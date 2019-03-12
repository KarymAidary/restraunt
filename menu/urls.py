from django.urls import path
from .views import DishUpdateView, basket_adding, remove_from_basket

app_name = 'menu'

urlpatterns = [
    path('add-to-basket/', basket_adding, name="add_to_basket"),
    path('remove-from-basket/', remove_from_basket, name="remove_from_basket"),
    
    path('<int:pk>/update/', DishUpdateView.as_view(), name='menu_detail'),
]

