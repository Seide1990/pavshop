from django.urls import path
from blog import views


app_name='blog'

urlpatterns = [
    path('', views.blog_detail, name='blog_detail'),
    path('blog_list/',views.blog_list,name='blog_list'),
]