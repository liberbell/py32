from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    # return HttpResponse("Welcome to Django page.")
    return render(request, 'blog/index.html')

posts =[
    {'author' : 'django1',
    'title': 'Blog Post1',
    'content' : 'First post content',
    'date_posted' : 'December 31, 2020'
    },
    {'author' : 'test user1',
    'title': 'Blog Post2',
    'content' : 'Second post content',
    'date_posted' : 'January 1, 2021'
    }
]
# def business(request):
#     return render(request, 'blog/business.html')

def business(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/business.html', context)