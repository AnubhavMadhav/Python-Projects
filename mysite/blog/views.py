from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})                  # to get dynamic html data
# or return render(request, 'index.html')           # if we do not want dynamic html template

def post(request):
    return HttpResponse("I'm a single post page.")