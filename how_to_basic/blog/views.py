from django.shortcuts import render
from .models import Blog
from . forms import BlogForm
from django.views.generic import UpdateView, ListView, DeleteView, CreateView , DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CreateBlog(CreateView):
    model = Blog
    success_url = reverse_lazy("index")
    fields = ["titulo", "subtitulo","cuerpo"]

class ListBlog(ListView):
    model = Blog
    template_name = "blog/list_blog.html"

class UpdateBlog(UpdateView):
    model = Blog
    success_url = reverse_lazy("index")
    fields = ["titulo", "subtitulo", "cuerpo"]

class DeleteBlog(DeleteView):
    model = Blog
    success_url = reverse_lazy("index")

class DetailBlog(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    fields = ['tiulo', 'subtitulo', 'cuerpo']