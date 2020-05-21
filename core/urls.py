from django.urls import path
from core.views import profileView, updateProfile

urlpatterns = [
    path('profile/<str:username>', profileView, name="profile"),
    path('updateprofile/', updateProfile, name="updateprofile"),
    # path('profile/', UserPostListView.as_view(), name="userpostlist")

]
