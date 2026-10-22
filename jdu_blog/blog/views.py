from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from .forms import PostForm, CommentForm


# 3-topshiriq: Ro'yxatdan o'tish (Register)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# 5-topshiriq: FBV ro'yxat sahifasiga @login_required qo'shish
@login_required
def post_list_fbv(request):
    posts = Post.objects.select_related('category', 'author').all()
    return render(request, 'blog/post_list.html', {'posts': posts})


# 5-topshiriq: CBV ro'yxat sahifasiga LoginRequiredMixin qo'shish
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.select_related('category', 'author').all()


# Bitta post sahifasi (Session orqali ko'rishlarni nazorat qilish, Like va Izohlar)
def post_detail(request, id):
    post = get_object_or_404(Post.objects.select_related('category', 'author'), id=id)

    # Ko'rishlar sonini cheklash (sahifani qayta-qayta yangilaganda o'smaydi)
    viewed_posts = request.session.get('viewed_posts', [])
    if post.id not in viewed_posts:
        post.views_count += 1
        post.save(update_fields=['views_count'])
        viewed_posts.append(post.id)
        request.session['viewed_posts'] = viewed_posts

    comments = post.comments.all().order_by('-created_at')

    is_liked = False
    if request.user.is_authenticated:
        is_liked = post.likes.filter(id=request.user.id).exists()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': form,
        'is_liked': is_liked,
    })


# Like bosish va qaytarib olish
@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'post_list'))
    return redirect(next_url)


# Yangi post yaratish
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


# Postni tahrirlash (to'g'rilangan dekorator)
@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})


# DRF API ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer