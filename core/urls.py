from django.urls import path
from core.views import profileView, updateProfile, home

urlpatterns = [
    path('profile/<str:username>', profileView, name="profile"),
    path('updateprofile/', updateProfile, name="updateprofile"),
    path('home/', home, name="home")
]
