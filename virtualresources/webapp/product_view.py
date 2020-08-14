from django.shortcuts import render, redirect
from .forms import CreateProductForm
from .models import Product
from django.contrib.auth.decorators import login_required
# Buy a product
# Shows the page where checkout page with the confirmation and stuff


@login_required(login_url="/signin")
def buy_product(request):
    product_id = request.GET.get("id")
    product = None
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        print(f"Could not find a product with id = {product_id}")

    if request.POST:
        # TODO do the checks like if user has enough money and stuff
        if True:
            return redirect(f"/checkout?id={product_id}")

    return render(request, "buy.html", {'product': product})

 
@login_required(login_url='/signin')
def checkout(request):
    prod_id = request.GET.get("id")
    product = None
    try:
        product =Product.objects.get(id = prod_id)
        # Do the same user currency checks here too

    except Product.DoesNotExist:
        print(f"Could not find {prod_id}")

    return render(request,"checkout.html",{'product':product})

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
            product: Product = product_creation_form.save(commit=False)
            product.seller = request.user
            product.save()

    return render(
        request,
        "sell.html",
        {'form': product_creation_form}
    )
