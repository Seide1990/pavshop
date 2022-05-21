from email.errors import MisplacedEnvelopeHeaderDefect
from itertools import product
from multiprocessing import context
from turtle import title
from unicodedata import name
from django.shortcuts import render
#from .forms import Comment_pro

from product.models import  Image_model, Product
#from product.models import Image_models
from django.http import HttpResponseRedirect

from .models import ShopCart
from .forms import  ShopCartForm

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def product_detail(request,id):
    context=dict()
    detail = Product.objects.get(id=id)
    image=Image_model.objects.filter(product_id=id)
    print(image)
    print(detail.name)
    form = ShopCartForm(instance=detail)
    context={'image':image ,'detail':detail,'form':form}
    #print(ShopCart.objects.filter(id))
    #print(Product.objects.get(id))
    if request.method=='POST':
        print(request.method)
        form = ShopCartForm(request.POST)
        info = ShopCart.objects.get(id=1)
        #sec=Product.objects.get(id=1)
        print(detail.name)
        #quantity=form.cleaned_data['quantity']
       
       # print(info)
        if form.is_valid():
            form=ShopCartForm(request.POST,instance=info)
          #  list = ShopCart(
            #    # quantity=quantity,
            #     title='seide',
            #     cart_id='2',
    
       # )
         #   list.save()
             
            form.save()  
       # 
        return render(request,'shopping-cart.html')
        
  
    print('bura geldi')
    return render(request,'product-detail.html',context)

def addtocart(request,id):
   
    #context=dict()
    instance = Product.objects.get(id=id)
    form = ShopCartForm(data=request.POST)
   # form = ShopCartForm(instance=instance)
    if request.method == 'POST':
        form = ShopCartForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            print('validden kecdi')
        return render(request,'shopping-cart.html')
    seide='salam necesen'
    context={'form':form,'seide':seide}
    return render(request,'product-list.html',context)
def product_list(request):
    contact_list =Product.objects.all()
    paginator = Paginator(contact_list, 1) 

    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
 #   form = ShopCartForm(data=request.POST)
  
  #  if request.method == 'POST':
   #     form = ShopCartForm(data=request.POST)
   #     if form.is_valid():
   #         form.save()
   #         print('validden kecdi')
   #     return render(request,'shopping-cart.html')
   # seide='salam necesen'
   # context={'form':form,'seide':seide,'product':product}
 # action="{% url 'product:shopping_cart' mehsul.id  %}"
    
    context={'product':product}
    return render(request,'product-list.html',context)

def shopping_cart(request):
    return render(request,'shopping-cart.html')





def comment(request):
    if request.method == 'POST':
        form = Comment_pro(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/product/')
    else:
        form = Comment_pro()
    return render(request,'product_detail.html',{'form':form})

