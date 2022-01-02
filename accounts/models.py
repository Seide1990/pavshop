from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
#class User(AbstractUser):
#    profile_photo=models.ImageField(null=True,blank=True,upload_to='media/')

    #class Meta:
     #   verbose_name="User"
      #  verbose_name_plural="User"



class User(AbstractUser):

    email = models.EmailField(_('email address'), blank=True, unique=True)
   
    phone=models.CharField( max_length=127, blank=True,null=True)
    adress=models.CharField(max_length=127, blank=True,null=True)
    country=models.CharField(max_length=127,null=True,blank=True, default='Azerbaidjan')
    city=models.CharField(max_length=127,null=True,blank=True,default='Baki')
  #  country=models.ForeignKey('Countries',on_delete=models.CASCADE,null=True, related_name='Countries')
  #  city=models.ForeignKey('Town',on_delete=models.CASCADE,null=True, related_name='Towns')


#class Countries(models.Model):
 #   country=models.CharField(max_length=127,null=True,blank=True, default='Azerbaidjan')
  #  def __str__(self):
   #      return self.country        # admin sehifesinde titleler gorunsun
#class Town(models.Model):
 #  city=models.CharField(max_length=127,null=True,blank=True,default='Baki')

  # def __str__(self):
   #      return self.city        # admin sehifesinde titleler gorunsun
   