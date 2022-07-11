from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm, CategoryForm

# def home(request):
#     return render(request, 'home.html')
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

class Homeview(ListView):
    model = Post
    ordering = ["-post_date", "-id"]


class ArticleDetailview(DetailView):
    model = Post


class AddCategoryView(CreateView):
    model = Category
    template_name = 'j.html'
    form_class = CategoryForm


class AddPostView(CreateView):
    model = Post
    form_class = PostForm


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
