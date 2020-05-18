from django.shortcuts import render, redirect, get_object_or_404, reverse
from Confession.models import ConfessionPost, Comment
from Confession.forms import CommentForm
from django.contrib import messages
from core.models import Profile
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class ConfessionPostList(ListView):
    queryset = ConfessionPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'confession/confessions.html'

class CreateConfessionPost(LoginRequiredMixin, CreateView):
    model = ConfessionPost
    fields = ['title', 'content', 'display_name']
    success_url = "/confessions/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = int(1)
        return super().form_valid(form)

@login_required
def confessionpost_detail(request, slug):
    post = get_object_or_404(ConfessionPost, slug=slug)
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None

            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None


            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment_name = request.user
                    replay_comment.parent = parent_obj
            new_comment = comment_form.save(commit=False)            
            new_comment.post = post
            new_comment.name = request.user
            
            new_comment.save()
            return redirect(reverse('confessions'))
    else:
        comment_form = CommentForm()
    return render(request,
                  'confession/confessionpost_detail.html',
                  {'confessionpost': post,
                   'comments': comments,
                   'comment_form': comment_form})

class CPUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ConfessionPost
    fields = ['title', 'content', 'display_name']
    success_url = "/confessions/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or post.display_name:
            return True
        return False


class CPDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ConfessionPost
    success_url = '/confessions/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or post.display_name:
            return True
        return False
