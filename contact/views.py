from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact.html')

def checkout(request):
    return render(request,'checkout.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')