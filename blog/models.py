from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class BlogPost(models.Model):
    
    title = models.CharField(max_length=200)
    teaser_blurb = models.CharField(max_length=200, default="Enter teaser blurb here.")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_published = models.BooleanField(default=False)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

