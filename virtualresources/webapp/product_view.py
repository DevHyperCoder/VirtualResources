from django.shortcuts import render, redirect
from .forms import CreateProductForm
from .models import Product
from django.contrib.auth.decorators import login_required
# Buy a product
# Shows the page where checkout page with the confirmation and stuff
@login_required(login_url="/signin")
def buy_product(request):
    return render(request, "checkout.html")

# Explore Products
def explore_product(request):
    return render(request,
                  "explore.html",
                  {'products': Product.objects.all()})

# Sell a product
# Make it login required
@login_required(login_url="/signin")
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