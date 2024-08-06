from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment-options', views.payment_options, name='payment_options'),
    path('confirm/', views.confirm_payment, name='confirm_payment'),
    path('success/', views.payment_success, name='payment_success'),
]
