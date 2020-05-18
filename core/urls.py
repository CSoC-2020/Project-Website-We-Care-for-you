from django.urls import path
from core.views import profileView

urlpatterns = [
    path('profile/<str:username>', profileView, name="profileof"),
    # path('profile/', ProfileView.as_view(), name="profile"),
    # path('profile/', UserPostListView.as_view(), name="userpostlist")

]
