from django.urls import path
from Confession.views import (
    ConfessionPostList, 
    ConfessionPostDetail,
    createConfessionPost,
)
urlpatterns = [
    path('confessions/', ConfessionPostList.as_view(), name='confessions'),
    path('confession/<slug:slug>/', ConfessionPostDetail.as_view(), name='confessionpost_detail'),
    path('create_confession_post/', createConfessionPost, name='create-confession-post'),

]