from django.shortcuts import render

# Create your views here.
def blog_detail(request):
    return render(request,'blog-detail.html')

def blog_list(request):
    return render(request,'blog-list.html')
