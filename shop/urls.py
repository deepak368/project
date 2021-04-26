"""MobileApplication URL Configuration

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
from django.shortcuts import render
from .views import brand_view,create_mobile,list_mobiles,brand_delete,brand_edit,mobile_detail,user_registration,\
    user_login,user_logout,order_details,error,cart

urlpatterns = [
    path("",lambda request:render(request,"shop/index.html")),
    path("brands/",brand_view,name="brandview"),
    path("mobiles",create_mobile,name="createmobile"),
    path("mobiles/list",list_mobiles,name="listmobiles"),
    path("delete/<int:id>",brand_delete,name="delete"),
    path("edit/<int:id>",brand_edit,name="edit"),
    path("mobiles/detail/<int:id>",mobile_detail,name="detail"),
    path("mobiles/userRegistration",user_registration,name="register"),
    path("mobiles/userlogin",user_login,name="userlogin"),
    path("mobiles/userlogout",user_logout,name="userlogout"),
    path("mobiles/order/<int:id>",order_details,name="order"),
    path("error",error,name="errorpg"),
    path("mobiles/order/cart",cart,name="cart")




]
