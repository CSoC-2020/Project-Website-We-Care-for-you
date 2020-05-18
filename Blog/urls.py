from django.urls import path
from Blog.views import (
    BlogPostList, 
    blogpost_detail,
    createBlogPost,
    BPUpdateView,
    BPDeleteView,
    
)
urlpatterns = [
    path('blogs/', BlogPostList.as_view(), name='blogs'),
    path('blog/<slug:slug>/', blogpost_detail, name='blogpost-detail'),
    path('create_blog_post/', createBlogPost, name='create-blog-post'),
    path('blogpost/<slug>/update', BPUpdateView.as_view(), name='blogpost-update'),
    path('blogpost/<slug>/delete', BPDeleteView.as_view(), name='blogpost-delete'),

]
