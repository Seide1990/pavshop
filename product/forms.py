from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#class ShopCartForm(ModelForm):
    
#    class Meta:
#        model=ShopCart
#        fields=['quantity']
#        Widgets={
#            'quantity': forms.TextInput(),
 #       }
