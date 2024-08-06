from django.contrib import admin
from .models import PaymentMethod, PaymentTransaction

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'cart', 'payment_method', 'amount', 'transaction_id', 'timestamp', 'is_successful')
    list_filter = ('is_successful', 'payment_method', 'timestamp')
    search_fields = ('transaction_id', 'user__username', 'cart__id')
