from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm

# 5-topshiriq: FBV da select_related ishlatish
def post_list_fbv(request):
    posts = Post.objects.select_related('category').all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# 5-topshiriq: CBV da select_related ishlatish
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.select_related('category').all()

# Detail view
def post_detail(request, id):
    post = get_object_or_404(Post.objects.select_related('category'), id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create view
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

# Update view

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        # instance=post — kiritilgan o'zgarishlarni aynan shu post ustiga yozadi
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)  # O'zgargan postning sahifasiga qaytadi
    else:
        # instance=post — mavjud sarlavha va matnni forma kataklariga avtomatik to'ldirib chiqaradi
        form = PostForm(instance=post)
        
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})