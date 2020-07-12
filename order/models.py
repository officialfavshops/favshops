from django.db import models
from cart.models import Cart
from address.models import Address
# Create your models here.
class Order(models.Model):

    order_id = models.CharField(max_length=30,null=True,blank=True)
    image = models.ImageField(upload_to='order_history_img',null=True,blank=True)
    mobile_number = models.CharField(max_length=15,null=True,blank=True)
    name = models.CharField(max_length=30,null=True,blank=True)
    brand = models.CharField(max_length=40,blank=True,null=True)
    quantity = models.CharField(max_length=20,null=True,blank=True)
    price = models.CharField(max_length=20,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    payment_mode = models.CharField(max_length=30,null=True,blank=True)

    

