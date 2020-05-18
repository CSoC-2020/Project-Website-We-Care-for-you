from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from core.models import Profile
from Blog.models import BlogPost, Images
from django.contrib.auth.models import User


@login_required
def profileView(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    posts = BlogPost.objects.filter(author=user)
    # post_images = Images.objects.filter(post=posts[0])  #Incomplete (rendering of images in blogpost)
    print ("this prints")
    context = {
        'user':user,
        'profile':profile,
        'posts':posts,
        'number_of_blogs':posts.count(),
        # 'post_images':post_images,
    }
    return render(request, 'profile.html', context)
# class ProfileView(DetailView):
#     model = Profile
#     template_name = "profile.html"
#     context_object_name = 'profile'
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Profile.objects.filter(user=user)



# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'profile.html', context)

# class UserPostListView(ListView):
#     model = BlogPost
#     template_name = 'profile.html'
#     context_object_name = 'blogposts'
#     paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return BlogPost.objects.filter(author=user).order_by('-date_posted')
