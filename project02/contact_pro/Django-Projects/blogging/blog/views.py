from django.shortcuts import render
from .models import*
from django.views.generic import ListView, DetailView
# Create your views here.

#postIndexview is a view
class PostIndexView(ListView):
    model= Blog
    template_name ='blog.html'
    queryset = Blog.objects.all()
    context_object_name ='posts'

class PostDetailView(DetailView):
    model = Blog
    context_object_name ='post'
    template_name ='blog-detail.html'

class BlogSearchView(ListView):
    model = Blog
    template_name ='blog.html'
    context_object_name='posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Blog.objects.filter(title_icontaions=query).order_by('-created_at') #display 