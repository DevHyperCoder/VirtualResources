from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import UserProfile,Product

# CreateProductForm 
class CreateProductForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    price = forms.IntegerField()
    desc = forms.CharField(max_length=500)

    class Meta:
        model = Product
        fields = [
            'name',
            'desc',
            'price'
        ]

# RegisterForm 
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=200)

    class Meta:
        model = UserProfile
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
