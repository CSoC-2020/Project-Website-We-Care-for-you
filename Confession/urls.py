from django.urls import path
from Confession.views import (
    ConfessionPostList, 
    confessionpost_detail,
    CreateConfessionPost,
    CPUpdateView,
    CPDeleteView,
)
urlpatterns = [
    path('confessions/', ConfessionPostList.as_view(), name='confessions'),
    path('confession/<slug:slug>/', confessionpost_detail, name='confessionpost-detail'),
    path('create_confession_post/', CreateConfessionPost.as_view(), name='create-confession-post'),
    path('confessionpost/<slug>/update', CPUpdateView.as_view(), name='confessionpost-update'),
    path('confessionpost/<slug>/delete', CPDeleteView.as_view(), name='confessionpost-delete'),

]