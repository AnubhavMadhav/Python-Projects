from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
# or return render(request, 'index.html', {})

def post(request):
    return HttpResponse("I'm a single post page.")