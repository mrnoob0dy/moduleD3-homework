from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView



class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')


class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


