from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<int:user_id>/', views.manageProfile, name='manage_profile'),
    path('category/<int:category_id>/', views.category_list, name='category_list'),
    path('food-items/', views.food_item_list, name='food_item_list'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('menu/', views.menu, name='menu'),
    path('book_tables/', include('book_tables.urls')),
    path('payment/', include('payment.urls')),
    path('about/', views.about, name='about'),

]
