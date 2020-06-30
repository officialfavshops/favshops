from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def user_register(request):
    return render(request,'register.html')

def user_login(request):
    return render(request,'login.html')

def wish_list(request):
    return render(request,'wishlist.html')

def forget_password(request):
    return render(request,'forget_password.html')