from django.db import models
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    image1=models.ImageField(upload_to='media/',null=True, blank=True)
    img1=models.ImageField(upload_to='media/',null=True, blank=True)
    img2=models.ImageField(upload_to='media/',null=True, blank=True)
    img3=models.ImageField(upload_to='media/',null=True, blank=True)
    haqqinda=models.TextField(default='Lorem ipsum dolor sit amet')
    name=models.TextField(help_text="name of the product")
    price=models.CharField(max_length=155,default='299$')
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
    
   
    
    def __str__(self):
        return 'name'
        
class Comment_model(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    message = models.TextField()
    
    def __str__(self):
        return 'name'