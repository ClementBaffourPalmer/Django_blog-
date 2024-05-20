from django.shortcuts import render
from django.views import generic
from .models import Post 


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post 
    template_name = 'post_detail.html'

def Post(request):
    posts = Post.objects.all() 
    return render(request, 'post_detail.html', {'posts': posts})

