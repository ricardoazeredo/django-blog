from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Post

def home(request):
    return HttpResponse("<h1>Ola Mundo!</h1>")

def post_list(request):
    post = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': post})