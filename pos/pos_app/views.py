from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def pos(request):
    products = Product.objects.all()
    return render(request, 'pos.html', {'products': products})

def process_order(request):
    if request.method == 'POST':
        total = 0
        cart = {}
        for product_id, quantity in request.POST.items():
            if product_id.isdigit():
                product = Product.objects.get(pk=product_id)
                total += product.price * int(quantity)
                cart[product.name] = int(quantity)
        return render(request, 'receipt.html', {'cart': cart, 'total': total})
