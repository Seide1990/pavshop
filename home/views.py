from django.core import paginator
from django.http import request
from django.shortcuts import render
from .models import Index
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
# class index(ListView):
#    model = Index    #index.objects.all alternativi

#    context_object_name = 'verilen'

#    template_name='index.html'
def index(request):
    contact_list = Index.objects.all()
    paginator = Paginator(contact_list, 1) 

    page = request.GET.get('page')
    try:
        verilen = paginator.page(page)
    except PageNotAnInteger:
        verilen = paginator.page(1)
    except EmptyPage:
        verilen = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'verilen': verilen})
#def index(request):
#    verilen=Index.objects.all
 #   context={'verilen':verilen}
 #   return render(request,'index.html',context)

def about_us(request):
    return render(request,'about-us.html')
