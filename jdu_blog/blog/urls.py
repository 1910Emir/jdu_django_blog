from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from .views import (
    post_list_fbv, 
    PostListView, 
    post_detail, 
    post_create, 
    post_update,
    register,
    PostViewSet,  # <-- 4-topshiriqda yaratilgan ViewSet
)

# 5-topshiriq: DRF Router yaratish va ro'yxatdan o'tkazish
router = DefaultRouter()
router.register('posts', PostViewSet, basename='post-api')

urlpatterns = [
    # DRF API endpointlari (http://127.0.0.1:8000/api/posts/)
    path('api/', include(router.urls)),

    # Ro'yxat sahifalari (Himoyalangan)
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('fbv/', post_list_fbv, name='post_list_fbv'),

    # Autentifikatsiya (3 va 4-topshiriq)
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Post amallari
    path('posts/new/', post_create, name='post_create'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('posts/<int:id>/edit/', post_update, name='post_update'),
]