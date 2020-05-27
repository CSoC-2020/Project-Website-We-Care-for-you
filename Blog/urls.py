from django.urls import path
from Blog.views import (
    BlogPostList, 
    blogpost_detail,
    createBlogPost,
    BPUpdateView,
    BPDeleteView,
    like_blogpost,
    
)

app_name = 'blog'

urlpatterns = [
    path('blogs/', BlogPostList.as_view(), name='posts'),
    path('blog/<slug:slug>/', blogpost_detail, name='post-detail'),
    path('blogpost/create/', createBlogPost, name='create-post'),
    path('blogpost/<slug>/update/', BPUpdateView.as_view(), name='post-update'),
    path('blogpost/<slug>/delete/', BPDeleteView.as_view(), name='post-delete'),
    path('blogpost/like/', like_blogpost, name='like-post'),

]
