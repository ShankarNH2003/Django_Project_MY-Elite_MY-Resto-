from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=True)
    is_employee = models.BooleanField('Is employee', default=False)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/')
    available = models.BooleanField('Available', default=False)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField('Available', default=False)
    image = models.ImageField(upload_to='food_images/')  # changed to singular 'image'

    def __str__(self):
        return self.name


