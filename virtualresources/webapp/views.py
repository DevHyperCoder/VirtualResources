from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import UserProfile
from django.contrib.auth import login,logout,authenticate,user_logged_in
from django.contrib.auth.forms import AuthenticationForm

# Home page
def home(request):
    print(request.user)
    return render(request,"home.html")

# Sign in route (LOGIN)
def sign_in(request):
    data =request.POST or None 
    form = AuthenticationForm(data = data)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        login(user = user,request = request)
        return redirect('home')
    
    return render(request,"signin.html",{'form':form})

# Sign up route (REGISTER)
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        
    return render(request,"register.html",{'form':form})


    

            
