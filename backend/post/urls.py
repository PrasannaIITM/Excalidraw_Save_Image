from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostView.as_view(), name= 'posts_list'),
    path('posts/<str:image>/', views.ImageView.as_view(), name = "image_view"),
    path('posts/download/<str:image>/', views.DownloadImageView.as_view(), name = "download_image_view"),
]