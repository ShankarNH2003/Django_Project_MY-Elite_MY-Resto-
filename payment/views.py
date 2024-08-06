from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from cart.models import Cart
from payment.models import PaymentTransaction  # Adjust import according to your actual cart app location

@login_required
def payment_options(request):
    cart = get_object_or_404(Cart, user=request.user, active=True)
    total_price = cart.get_total_price()  # Call the method if it's a method

   
    return render(request, 'payment/payment_options.html', {'total_price': total_price})
    
@login_required
def confirm_payment(request):
    cart = Cart.objects.get(user=request.user)
    total_amount = cart.get_total_price()
    
    # Assuming payment processing is done here
    # For example, you might use an API to handle the payment

    # Simulate a successful payment response
    payment_successful = True  # This should be the result of the payment API call
    
    if payment_successful:
        transaction_id = "example_transaction_id"  # This should come from the payment API response

        PaymentTransaction.objects.create(
            user=request.user,
            cart=cart,
            amount=total_amount,
            transaction_id=transaction_id,
            is_successful=True
        )
        return redirect('payment:payment_success')
    else:
        # Handle payment failure
        return redirect('payment:payment_failure')

@login_required
def payment_success(request):
    return render(request, 'payment/payment_success.html')
