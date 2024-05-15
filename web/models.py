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

class Tvets(models.Model):
    name= models.CharField(max_length=150)
    class Meta:
        verbose_name_plural = "Tvets"
    
    def __str__(self):
        return self.name

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

class Profile(models.Model):
    current_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='images/userprofiles')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    tvets = models.ForeignKey(Tvets, null=True, blank=True, on_delete=models.CASCADE)
    location= models.CharField(max_length=50)
    job_title= models.CharField(max_length=50)
    bio = models.TextField(null=True)
    date_of_birth = models.DateField()


    class Meta:
        verbose_name_plural = "User Profile"
    
    def __str__(self):
        return str(self.current_user)

class SubCategory(models.Model):
    sub_category= models.CharField(max_length=50)
    main_category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "SubCategories"
    
    def __str__(self):
        return self.sub_category
    
class WhyChoose(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/category/')
    title= models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Why Choose Us"
    
    def __str__(self):
        return self.title