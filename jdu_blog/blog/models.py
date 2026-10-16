from django.db import models

# 3-topshiriq: Bog'liq Category modeli
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")

    # 4-topshiriq: Category uchun __str__ metodi
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 3-topshiriq: ForeignKey bog'lanishi
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='posts',
        null=True, 
        blank=True,
        verbose_name="Kategoriya"
    )

    # 4-topshiriq: Asosiy model uchun __str__ metodi
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='posts',
        null=True, 
        blank=True,
        verbose_name="Kategoriya"
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Faqat birinchi marta yaratilganda saqlanadi
    updated_at = models.DateTimeField(auto_now=True)      # Har safar o'zgartirilganda vaqt avtomatik yangilanadi

    def __str__(self):
        return self.title