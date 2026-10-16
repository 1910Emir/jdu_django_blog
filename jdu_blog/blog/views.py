from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Post
from .forms import PostForm

# 3-topshiriq: Ro'yxatdan o'tish (Register)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Ro'yxatdan o'tgach, darhol tizimga kiritish
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# 5-topshiriq: FBV ro'yxat sahifasiga @login_required qo'shish
@login_required
def post_list_fbv(request):
    posts = Post.objects.select_related('category').all()
    return render(request, 'blog/post_list.html', {'posts': posts})


# 5-topshiriq: CBV ro'yxat sahifasiga LoginRequiredMixin qo'shish
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.select_related('category').all()


# Bitta post sahifasi
def post_detail(request, id):
    post = get_object_or_404(Post.objects.select_related('category'), id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


# Yangi post yaratish (bunga ham login talab qilinishi ma'qul)
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


# Postni tahrirlash
@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})