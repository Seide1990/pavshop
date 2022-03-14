from django.urls import path
from order import views

app_name='order'

urlpatterns=[
    path('shop_cart/<int:id>',views.shop_cart_list,name='shopcart'),
    path('addtocart/',views.shop_cart_add,name='addtocart'),
    path('deletefromcart/<int:id>',views.shop_cart_delete,name='deletefromcart'), 
]
