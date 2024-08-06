# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:item_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart_view, name='remove_from_cart_view'),
    path('confirm/', views.confirm_order_view, name='confirm_order_view'),
    # path('order-confirmation/', views.order_confirmation, name='order_confirmation_view'),
]
