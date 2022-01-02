from django import forms
from product.models import Comment_model

class Comment_pro(forms.ModelForm):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email')  
      message = forms.CharField(widget=forms.Textarea)