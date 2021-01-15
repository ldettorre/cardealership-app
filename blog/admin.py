from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'published_date', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 20
    search_fields = ('id', 'title', 'tags',)
admin.site.register(BlogPost, BlogPostAdmin)