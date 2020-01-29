from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class HeaderText(models.Model):
    name = models.CharField(max_length=50)
    txt1 = models.CharField(max_length=50)
    txt2 = models.CharField(max_length=50)
    txt3 = models.CharField(max_length=50)
    

class Posts(models.Model):
    title = models.CharField(max_length=70)
    excrept = models.CharField(max_length=125)
    slug = models.SlugField(max_length=70)
    body = RichTextField()
    date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    thumb = models.ImageField(default= False, upload_to= 'media/')
    def __str__(self):
        return self.title