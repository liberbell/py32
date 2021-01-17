from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
def index(request):
    # return HttpResponse("Welcome to Django page.")
    return render(request, 'blog/index.html')

def business(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/business.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/business.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
        return True
    else:
        return False