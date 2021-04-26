from django.shortcuts import render,redirect
from shop.forms import BrandCreateForm,MobileCreateForm,BrandEditForm,OrderForm
from .models import Brand,Mobile,Order
from .forms import UserRegForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

# Create your views here.

def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return  redirect("errorpg")
        else:
            return func(request)
    return wrapper
def permission_needed(func):
    def wrapper(a,b):
        if not a.b.user.is_superuser:
            return redirect("errorpg")
        else:
            return func(a,b)
    return wrapper

@admin_permission_required
def brand_view(request):

    brands=Brand.objects.all()
    form=BrandCreateForm()
    context={}
    context["brands"]=brands
    context["form"]=form
    if request.method=="POST":
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("brandview")
    return render(request,'shop/bndcreate.html',context)


def error(request):
    return render(request, "shop/errorpage.html")

@admin_permission_required
def create_mobile(request):
    form=MobileCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=MobileCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("createmobile")
    return render(request,'shop/mobilecreate.html',context)


def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"shop/listmobiles.html",context)
@permission_needed
def brand_delete(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("brandview")
@permission_needed
def brand_edit(request,id):
    brand=Brand.objects.get(id=id)
    form=BrandCreateForm(instance=brand)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandCreateForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect("brandview")
    return render(request,"shop/brandedit.html",context)

def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"shop/mobiledetail.html",context)

def user_registration(request):
    form=UserRegForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
    return render(request,"shop/userreg.html",context)

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request, "shop/login.html")


    return render(request,"shop/login.html")

def user_logout(request):
    logout(request)
    return redirect("userlogin")

def order_details(request,id):
    product=Mobile.objects.get(id=id)
    form=OrderForm(initial={"user":request.user,"product":product})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cart")
        else:
            form
    return render(request,"shop/order.html",context)

def cart(request):
    username=request.user
    orders=Order.objects.all().filter(user=username)
    context={}
    context["orders"]=orders
    return render(request,"shop/cart.html",context)





