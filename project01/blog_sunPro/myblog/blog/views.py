from django.shortcuts import render  , redirect
from .models import BlogPost

# Create your views here.
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get['title']
        content = request.POST.get['content']
        BlogPost.objects.create(title=title, content=content)
        return redirect(request,'show_post')
    return render(request, 'create_post.html')

def show_posts(request):
    posts = BlogPost.objects.all
    return render(request, 'show_posts.html',{'posts': posts})