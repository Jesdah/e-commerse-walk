from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NqyOeCX0OehRMtgvbMQbd1KE8oxYGm7ctq03axp1bxl8Zm1x6b4Bw9uDqJBXIEE2C6jfsdNXFifK6xEFJQtC23100EigYKJUw',
        'client_secret': 'client secret key',
    }

    return render(request, template, context)