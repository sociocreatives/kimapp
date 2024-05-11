from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Legal(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    class Meta:
        verbose_name_plural = "Legal"
    
    def __str__(self):
        return self.title

class Faqs(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    class Meta:
        verbose_name_plural = "Faqs"
    
    def __str__(self):
        return self.title

class ExpertTips(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/blog/')

    class Meta:
        verbose_name_plural = "Expert Tips"
    
    def __str__(self):
        return self.title

class Category(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/category/')
    name= models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Main Categories"
    
    def __str__(self):
        return self.name

class MajorCategory(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/category/subcats')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Major Sub Categories"
    
    def __str__(self):
        return self.name