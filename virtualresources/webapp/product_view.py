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
# Make it login required
def sell_product(request):
    product_creation_form = CreateProductForm(request.POST or None)
    if request.method == "POST":
        print("POSTED")
        if product_creation_form.is_valid():
            # product_creation_form
            print("form is valid")
            product :Product= product_creation_form.save(commit = False)
            product.seller = request.user
            product.save()
            
            

    return render(
        request,
        "sell.html",
        {'form':product_creation_form}
    )