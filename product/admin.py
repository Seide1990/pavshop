from django.contrib import admin

# Register your models here.
from.models import Product
admin.site.register(Product)

from .models import Comment_model
admin.site.register(Comment_model)

from .models import Image_model
admin.site.register(Image_model)


