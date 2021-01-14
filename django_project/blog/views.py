from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView


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