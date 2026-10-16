from django.urls import path
from .views import post_list_fbv, PostListView, post_detail, post_create

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new/', post_create, name='post_create'),          # <-- 6-hafta formasi
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('fbv/', post_list_fbv, name='post_list_fbv'),
    path('cbv/', PostListView.as_view(), name='post_list_cbv'),
]