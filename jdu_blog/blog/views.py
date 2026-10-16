from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def post_list_fbv(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'