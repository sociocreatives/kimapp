from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Colleges(models.Model):
    name= models.CharField(max_length=150)
    class Meta:
        verbose_name_plural = "Tvets"
    
    def __str__(self):
        return self.name



class CategoryUganda(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/category/')
    name= models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Main Categories"
    
    def __str__(self):
        return self.name

class MajorCategoryUganda(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/category/subcats')
    category = models.ForeignKey(CategoryUganda, null=True, blank=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Major Sub Categories"
    
    def __str__(self):
        return self.name


class SubCategoryUganda(models.Model):
    sub_category= models.CharField(max_length=50)
    main_category = models.ForeignKey(CategoryUganda, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "SubCategories"
    
    def __str__(self):
        return self.sub_category
    
