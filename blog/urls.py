from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'blog-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'blog-update'),
    path('post/create/', PostCreateView.as_view(), name = 'blog-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'blog-detail'),
    path('', PostListView.as_view(), name="blog-home"),
    path('about/', views.about, name="blog-about"),
]