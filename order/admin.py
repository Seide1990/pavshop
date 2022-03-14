from django.contrib import admin

# Register your models here.
from.models import shoppingCartItem,shoppingCart
admin.site.register(shoppingCartItem)
admin.site.register(shoppingCart)
