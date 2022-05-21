
from ast import Delete
from audioop import reverse
from email import message
from itertools import product
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
import re
from django.http import request
from django.shortcuts import redirect, render

from django.urls import reverse_lazy

# Create your views here.

   
#def addtocart(request):
 #   form = ShopCartForm()
  #  if request.method == 'POST':
  #      form = ShopCartForm(data=request.POST)
  #      if form.is_valid():
  #          form.save()
  #      return render(request,'sopping-cart.html')
  #  return render(request,'product-detail.html',{'form':form})


        
#@login_required(login_url='/login')
#def shop_cart_add(request,proid):
#    url=request.META.get('HTTP_REFERER')
#    form=ShopCartForm(request.POST or None)
#    if request.method=='POST':
#        if form.is_valid():
#            current_user=request.user
#            quantity=form.cleaned_data['quantity']
#            try:
#                q1=ShopCart.objects.get(user_id=current_user.id,product_id=proid)
#            except ShopCart.DoesNotExist:
#                q1=None
#            if q1!=None:
#                q1.quantity=q1.quantity+quantity
#                q1.save()
#            else:
#                data=ShopCart.objects.create(user_id=current_user.id,product_id=proid,quantity=quantity)

 #           request.session['cart_items']=ShopCart.objects.filter(user_id=current_user.id).count()
 #           messages.success(request,'product add to cart')
 #           return HttpResponseRedirect(url)
 #   return HttpResponseRedirect(reverse('product',args=[proid]))
    


#@login_required(login_url='/login')
def shop_cart_list(request):
    current_user=request.user
    shopcart= ShopCart.object.all().filter(user_id=current_user.id)
    carttotal=()
    for rs in shopcart:
        carttotal+=rs.quantity*rs.product.price
    
    context={ 'pace':'cart',
    'shopcart':'shopcart',

    }
