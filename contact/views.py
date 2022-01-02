from django.shortcuts import render


# Create your views here.
def contact(request):
    return render(request,'contact.html')

def checkout(request):
    return render(request,'checkout.html')



