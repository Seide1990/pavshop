from pickle import TRUE
from re import T
from unicodedata import category
from django.db import models
from django.db.models.aggregates import Count
from django.utils.text import slugify
# Create your models here.
class ShopCart(models.Model):
       title=models.CharField(max_length=100, blank=True, null=True)
       cart_id = models.CharField(max_length=100)
       quantity= models.IntegerField(default=1)
     #  quantity=models.ForeignKey('Quantity',on_delete=models.CASCADE,null=True, related_name='Quantities',default=1)
   # full_name = models.CharField(max_length=100, blank=True, null=True)
   # email = models.CharField(max_length=100, blank=True, null=True)
   # message = models.TextField()
   # subject = models.CharField(max_length=100,)

      # def __str__(self):
      #      return self.quantity

#class Quantity(models.Model):
 #   quantity=models.IntegerField(default=1)
class Category(models.Model):
    name=models.CharField(max_length=155)
    slug=models.SlugField(null=False,blank=True,unique=True,max_length=50)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
   
    def __str__(self):
        return self.name
class Brand(models.Model):
    name=models.CharField(max_length=155)
    slug=models.SlugField(null=False,blank=True,unique=True,max_length=50)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
   
    def __str__(self):
        return self.name
class Product(models.Model):
    image1=models.ImageField(upload_to='media/',null=True, blank=True)
    Category=models.ForeignKey(Category,null=TRUE,on_delete=models.DO_NOTHING)
   # tag=models.ForeignKey(Tag,null=TRUE,on_delete=models.DO_NOTHING)
    haqqinda=models.TextField(default='Lorem ipsum dolor sit amet')
    name=models.CharField(max_length=155)
    price=models.CharField(max_length=155,default='299$')
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    designer=models.CharField(max_length=155,default='ABCart')
    brand=models.ForeignKey(Brand,null=TRUE,on_delete=models.DO_NOTHING)
    Count=models.BigIntegerField()
    informations=models.TextField(help_text='mehsul haqqinda melumat')
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
        

        
        
class Comment_model(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    message = models.TextField()
    
    def __str__(self):
        return 'name'
class Image_model(models.Model):
    img=models.ImageField(upload_to='media/',null=True, blank=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True, related_name='products')
    
    def __str__(self):
        return self.product.name

