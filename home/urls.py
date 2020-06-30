
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user_register',views.user_register,name='user_register'),
    path('user_login',views.user_login,name='user_login'),
    path('wish_list',views.wish_list,name='wish_list'),
    path('forget_password',views.forget_password,name='forget_password'),
]