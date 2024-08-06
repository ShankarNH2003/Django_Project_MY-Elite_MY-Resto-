from django.contrib import admin

# Register your models here.
from .models import FoodCategory, FoodItem,User

admin.site.register(User)
admin.site.register(FoodCategory)
admin.site.register(FoodItem)

