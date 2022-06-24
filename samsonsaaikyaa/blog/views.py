from pyexpat import model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
 
class PostCreatView(CreateView):

    model = Post
    field = [
        "__all__"
    ]
    success_url: reverse_lazy("blog:all")
 
class PostListView(ListView):

    model = Post

class PostDetailView(DetailView):
    model: Post

class PostUpdateView(UpdateView):
    model: Post
    field = [
        "__all__"
    ]
    success_url: reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model: Post
    field = [
        "__all__"
    ]
    success_url: reverse_lazy("blog:all")

    

    
 
