from django.urls import path
from home import views

app_name='home'

urlpatterns=[
    path('',views.index,name='index'),
    path('about_us/',views.about_us,name='about_us')

]