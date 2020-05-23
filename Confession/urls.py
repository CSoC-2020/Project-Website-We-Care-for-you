from django.urls import path
from Confession.views import (
    ConfessionPostList, 
    confessionpost_detail,
    CreateConfessionPost,
    CPUpdateView,
    CPDeleteView,
    like_confessionpost,
)

app_name = 'confession' 

urlpatterns = [
    path('confessions/', ConfessionPostList.as_view(), name='posts'),
    path('confessionpost/<slug:slug>/', confessionpost_detail, name='post-detail'),
    path('create_confessionpost/', CreateConfessionPost.as_view(), name='create-post'),
    path('confessionpost/<slug>/update', CPUpdateView.as_view(), name='post-update'),
    path('confessionpost/<slug>/delete', CPDeleteView.as_view(), name='post-delete'),
    path('like_confessionpost/', like_confessionpost, name='like-post'),

]