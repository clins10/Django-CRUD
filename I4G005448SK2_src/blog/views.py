from telnetlib import STATUS
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Post

# from I4G005448SK2_src.blog.models import Post


# creating classes
class PostListView(ListView):
    model = Post
    # def get_queryset(self):
    #     return super().queryset().filter(STATUS = 'Published')
    # paginate_by: 3
        


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')


class PostDetailView(DetailView):
    model = Post
    


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')


class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
