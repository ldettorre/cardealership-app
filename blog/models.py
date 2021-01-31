from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class BlogPost(models.Model):
    
    title = models.CharField(max_length=200)
    def upload_photo_to(self, filename):
        return f'{self.title}/{filename}'
    teaser_blurb = models.CharField(max_length=200, default="Enter teaser blurb here.")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_published = models.BooleanField(default=False)
    tag = models.CharField(max_length=30, blank=True, null=True)
    photo_1 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_2 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_3 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_4 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_5 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_6 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_7 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_8 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_9 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_10 = models.ImageField(upload_to=upload_photo_to, blank=True)

