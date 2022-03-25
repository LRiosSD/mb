from time import clock_settime
from django.views.generic.edit import CreateView
from django.views.generic  import ListView, DetailView
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'text']