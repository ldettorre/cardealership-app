from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.

def blog(request):
    blogposts = BlogPost.objects.all()
    blogposts = blogposts.filter(is_published=True)
    return render(request, 'blog/blog.html', {"blogposts":blogposts})
    

def blog_post(request,blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog/blog_post.html', {"blog": blog})