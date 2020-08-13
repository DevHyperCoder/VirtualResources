from django.shortcuts import render,redirect

# About page
def about_page(request):
    return render(request,"about.html")

# Contact page
def contact_page(request):
    return render(request,"contact.html")