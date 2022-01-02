from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
admin.site.register(User)
#from .models import Countries
#admin.site.register(Countries)
#from .models import Town
#admin.site.register(Town)
