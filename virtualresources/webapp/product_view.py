from django.shortcuts import render, redirect
from .forms import CreateProductForm
from .models import Product

# Buy a product
# Shows the page where checkout page with the confirmation and stuff
def buy_product(request):
    return render(request, "checkout.html")

# Explore Products
def explore_product(request):
    return render(request,
                  "explore.html",
                  {'products': Product.objects.all()})

# Sell a product