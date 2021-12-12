from django.shortcuts import render

# Create your views here.
def product_detail(request):
    return render(request,'product-detail.html')

def product_list(request):
    return render(request,'product-list.html')

def shopping_cart(request):
    return render(request,'shopping-cart.html')