from django.urls import path
from home import views

app_name='home'

urlpatterns=[
    path('',views.index,name='index'),   # .as_view(),
    path('about_us/',views.about_us,name='about_us')

]