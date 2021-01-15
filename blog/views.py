from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.

def blog(request):
    blogpost = BlogPost.objects.all()
    return render(request, 'blog/blog.html', {"blogpost":blogpost})
    

def blog_post(request,blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog/blog_post.html', {"blog": blog})