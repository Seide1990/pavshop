from django.urls import path
from product import views
#from order.views import addtocart
app_name='product'

urlpatterns=[
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),
   # path('product_detail/<int:id>/',addtocart,name='product_detail'),
    path('product_list/',views.product_list,name='product_list'),
    path('shopping_cart/<int:id>/',views.addtocart,name='shopping_cart'),
    path('category/<slug:Category_slug>/',views.product_category,name='product_category'),
    path('brand/<slug:brand_slug>/',views.product_brand,name='product_brand')
]