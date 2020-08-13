"""virtualresources URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import product_view,views,reach_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name ="home"),
    path("register",views.register,name = "register"),
    path("signin",views.sign_in,name ="sign_in"),
    path("explore",product_view.explore_product,name = "explore"),
    path("about",reach_views.about_page,name = "about_page"),
    path("contact",reach_views.contact_page,name = "contact_page")
]