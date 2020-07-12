from django.shortcuts import render,redirect
from Products.forms import Product_form
from Products.models import Product
from django.contrib import messages
from cart.models import Cart
from order.models import Order

# Create your views here.

def index(request):
    special_offer = Product.objects.filter(special_offer=True).order_by('-upload_time')
    cartlen = 0
    cart = None
    if request.user.is_authenticated:
        mnumber = request.user.mobile_number
        cart = Cart.objects.filter(mobile_number = mnumber)
        cartlen = len(cart)
    return render(request,'index.html',{'special_offer':special_offer,'cartlen':cartlen,'cart':cart})

def cart_page(request):
    mnumber = request.user.mobile_number
    total = 0
    cart = Cart.objects.filter(mobile_number = mnumber).order_by('-add_time')
    for data in cart:
        total += int(data.product.discount_price) * int(data.product.quantity.split(' ')[0])
    return render(request,'cart.html',{'cart':cart,'total':total})

def user_register(request):
    return render(request,'register.html')

def user_login(request):
    return render(request,'login.html')

def wish_list(request):
    return render(request,'wishlist.html')

def forget_password(request):
    return render(request,'forget_password.html')

def admin_page(request):
    
    return render(request,'admin_page.html')

def about(request):
    return render(request,'about.html')

def order_history(request):
    mnumber = request.user.mobile_number
    orders = Order.objects.filter(mobile_number = mnumber).order_by('-date')
    total = 0
    for ord in orders:
        total += int(ord.price)

    return render(request,'order_history.html',{'orders':orders,'total':total})

def contact(request):
    return render(request,'contact.html')

def profile_page(request):
    user = request.user
    return render(request,'profile.html')

def product_details(request,pk):
    prod = Product.objects.get(pk=pk)
    return render(request,'product_details.html',{'product':prod})