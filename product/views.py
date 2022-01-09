from django.shortcuts import render
from .forms import Comment_pro

from product.models import  Image_model, Product
#from product.models import Image_models
from django.http import HttpResponseRedirect


from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def product_detail(request,id):
    detail = Product.objects.get(id=id)
    image=Image_model.objects.filter(product_id=id)
    print(image)
    context={'image':image ,'detail':detail}
    return render(request,'product-detail.html',context)

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