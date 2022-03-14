from django import forms
from django.forms import ModelForm,TextInput

from order.models import ShopCart
#class Comment_pro(forms.ModelForm):
#      name = forms.CharField(required=False)
#      email = forms.EmailField(label='Your email')  
#      message = forms.CharField(widget=forms.Textarea)
class ShopCartForm(ModelForm):
    class Meta:
        #model=ShopCart
        fields=['quantity']
        Widgets= {'quantity': TextInput(attrs={'class': 'input', 'type':'number', 'value':1})}
