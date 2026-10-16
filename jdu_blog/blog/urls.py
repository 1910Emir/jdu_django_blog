from django.urls import path
from .views import post_list_fbv, PostListView

urlpatterns = [
    path('fbv/', post_list_fbv, name='post_list_fbv'),
    path('cbv/', PostListView.as_view(), name='post_list_cbv'),
]