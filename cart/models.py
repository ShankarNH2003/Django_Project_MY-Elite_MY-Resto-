# cart/models.py
from django.db import models
from django.conf import settings
from main.models import FoodItem  # Import FoodItem from the main app

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use 'user' for the relationship
    active = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def get_total_price(self):
        return sum(item.quantity * item.item.price for item in self.cart_items.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')  # Fix related_name conflict
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)  # Use 'item' instead of 'food_item'
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # User who placed the order
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total cost of the order
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the order was created
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  # Reference to the order
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)  # Reference to the food item
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the item

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'