from django.urls import path
from Blog.views import (
    BlogPostList, 
    BlogPostDetail,
    createBlogPost,
)
urlpatterns = [
    path('blogs/', BlogPostList.as_view(), name='blogs'),
    path('blog/<slug:slug>/', BlogPostDetail.as_view(), name='blogpost_detail'),
    path('create_blog_post/', createBlogPost, name='create-blog-post'),

]
