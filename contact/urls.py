from django.urls import path
from contact import views

app_name='contact'

urlpatterns=[
    path('',views.contact,name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
]