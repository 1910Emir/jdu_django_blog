from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Post(models.Model):
    # Post egasi (tizimdagi foydalanuvchi, bo'sh bo'lishi ham mumkin)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name="Muallif"
    )
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Post mazmuni")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name="Kategoriya"
    )
    image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name="Post rasmi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    views_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    likes = models.ManyToManyField(User, related_name='blog_posts_liked', blank=True, verbose_name="Likelar")

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Muallif")
    text = models.TextField(verbose_name="Izoh matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yozilgan vaqti")

    def __str__(self):
        return f"{self.author.username} - {self.post.title}"

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"