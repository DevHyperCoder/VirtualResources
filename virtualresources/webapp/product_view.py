from django.shortcuts import render, redirect
from .forms import CreateProductForm
from .models import Product, UserProfile
from django.contrib.auth.decorators import login_required

def enough_money_in_user(user:UserProfile,amt:int):
    money = user.money
    if (money>=amt):
        return True
    
    return False


# Buy a product
# Shows the page where checkout page with the confirmation and stuff
@login_required(login_url="/signin")
def buy_product(request):
    product_id = request.GET.get("id")
    product:Product = None
    try:
        product = Product.objects.get(id=product_id) 
    except Product.DoesNotExist:
        print(f"Could not find a product with id = {product_id}")

    if request.POST:
        # TODO do the checks like if user has enough money and stuff
        if request.user.id == product.seller.id :
            # Same user
            return render(request,"buy.html",{"product":product,"same_user":"asdf"})
        if enough_money_in_user(request.user,product.price):
            # Deduct from the user
            user:UserProfile = request.user
            old_bal_user = user.money
            new_bal_user = old_bal_user - product.price
            user.money = new_bal_user
            user.save()

            # Add the money to the seller
            seller = product.seller
            old_bal_seller = seller.money
            new_bal_seller = old_bal_seller+product.price
            seller.money = new_bal_seller
            seller.save()

            # TODO Remove from cart list if exists

            return redirect(f"/checkout?id={product_id}")
        else:
            return render(request,"buy.html",{"product":product,"not_enough_error":"asdf"})

    return render(request, "buy.html", {'product': product})

 
@login_required(login_url='/signin')
def checkout(request):
    prod_id = request.GET.get("id")
    product = None
    try:
        product =Product.objects.get(id = prod_id)
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
