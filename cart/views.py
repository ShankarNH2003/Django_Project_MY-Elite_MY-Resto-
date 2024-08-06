
from django.utils.translation import gettext_lazy as _

# cart/views.py


from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from main.models import FoodItem
from .models import Cart, CartItem, Order, OrderItem
from django.db.models import F

@login_required
def add_to_cart_view(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    quantity = int(request.POST.get('quantity', 1))
    
    # Get or create the cart for the user
    cart, created = Cart.objects.get_or_create(user=request.user, active=True)
    
    # Get or create the cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        item=item,
        defaults={'quantity': quantity}
    )
    
    if not created:
        # If the item already exists in the cart, update the quantity
        cart_item.quantity = F('quantity') + quantity
        cart_item.save()
    
    # Update the total price of the cart
    cart.total_price = sum(item.item.price * item.quantity for item in cart.cart_items.all())
    cart.save()
    
    return redirect('cart:cart_view')

@login_required
def cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user, active=True)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user, active=True)
    
    cart_items = cart.cart_items.all()
    
    # Calculate the total price for each item and the overall total price
    for item in cart_items:
        item.total_price = item.item.price * item.quantity
    
    total_price = sum(item.total_price for item in cart_items)
    
    if request.method == 'POST':
        # Create an order with the total price
        order = Order.objects.create(user=request.user, total_price=total_price)

        # Add items to the order
        for item in cart_items:
            OrderItem.objects.create(order=order, item=item.item, quantity=item.quantity)
        
        # Clear the cart
        cart.cart_items.all().delete()
        cart.total_price = 0
        cart.active = False
        cart.save()
        
        # Redirect to payment options page with total price
        return redirect('payment:payment_options', total_price=total_price)    
    return render(request, 'cart/cart_view.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def remove_from_cart_view(request, item_id):
    cart = Cart.objects.get(user=request.user, active=True)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_view')


@login_required
def confirm_order_view(request):
    try:
        cart = Cart.objects.get(user=request.user, active=True)
    except Cart.DoesNotExist:
        return redirect('cart:cart_view')  # Redirect to cart view if no active cart
    
    cart_items = cart.cart_items.all()
    total_price = sum(item.quantity * item.item.price for item in cart_items)
    
    if request.method == 'POST':
        # Create an order with the total price
        order = Order.objects.create(user=request.user, total_price=total_price)

        # Add items to the order
        for item in cart_items:
            OrderItem.objects.create(order=order, item=item.item, quantity=item.quantity)

        # Clear the cart
        cart.cart_items.all().delete()
        cart.total_price = 0
        cart.active = True
        cart.save()
        
        # Redirect to payment options page
        return redirect('payment:payment_options')
 
    return render(request, 'cart/confirm_order.html', {'cart_items': cart_items, 'total_price': total_price})
