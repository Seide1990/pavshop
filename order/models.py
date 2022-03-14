
from itertools import product
from telnetlib import STATUS
from turtle import update
from django.contrib.auth.models import User
from django.db import models
from product.models import Product
from django.contrib.auth import get_user_model
from django.conf import settings

class shoppingCartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.FloatField()
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.product.name

class shoppingCart(models.Model):
    user=models.ForeignKey(to=settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    items=models.ManyToManyField(shoppingCartItem, blank=True)
    total_price=models.FloatField()
    #status=models.CharField(default="waiting", choices=STATUS,max_length=10,)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
    
        return self.user.email
#class ShopCart(models.Model):
 #   user=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
   # product=models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
  #  quantity=models.IntegerField()
   # name=models.CharField(max_length=155)
   # price=models.CharField(max_length=155,default='299$')
   # def __str__(self):
   #     return self.product
   # @property
   # def amount(self):
   #     return (self.quantity*self.product.price)
