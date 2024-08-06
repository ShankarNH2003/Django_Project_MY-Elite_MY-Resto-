from django.db import models
from django.conf import settings
from cart.models import Cart  # Adjust import according to your actual cart app location

class PaymentMethod(models.Model):
    """Model to store different payment methods."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PaymentTransaction(models.Model):
    """Model to store payment transaction details."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {'Success' if self.is_successful else 'Failed'}"
