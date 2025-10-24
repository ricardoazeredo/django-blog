from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    post = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': post})