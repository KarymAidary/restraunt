from django.urls import path
from .views import MainView, CartView

app_name = 'core'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('cart/', CartView.as_view(), name='basket'),
]
