from django.urls import path
from . import views


urlpatterns = [
    path('reserve/', views.reserve_table, name='reserve_table'),
    path('available/', views.view_available_tables, name='view_available_tables'),
    path('reservation_confirmation/', views.reservation_confirmation, name='reservation_confirmation'),
]
