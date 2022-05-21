from django.db import models
from django.db.models.aggregates import Count
from django.utils.text import slugify
# Create your models here.
class ShopCart(models.Model):
       title=models.CharField(max_length=100, blank=True, null=True)
       cart_id = models.CharField(max_length=100)
       quantity=models.IntegerField(default=1)
   # full_name = models.CharField(max_length=100, blank=True, null=True)
   # email = models.CharField(max_length=100, blank=True, null=True)
   # message = models.TextField()
   # subject = models.CharField(max_length=100,)

      # def __str__(self):
      #      return self.quantity




class Product(models.Model):
    image1=models.ImageField(upload_to='media/',null=True, blank=True)

    haqqinda=models.TextField(default='Lorem ipsum dolor sit amet')
    name=models.CharField(max_length=155)
    price=models.CharField(max_length=155,default='299$')
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    designer=models.CharField(max_length=155,default='ABCart')
    brand=models.CharField(max_length=250,blank=True,null=True,default='---')
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

