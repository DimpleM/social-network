from django.shortcuts import render
from .models import Post
from users.models import Profile
from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.conf import settings


def home(request):
    profile = Profile.objects.get(user=request.user)
    users = [user for user in profile.following.all()]
    print(users)
    posts = []
    for user in users:
        p = Profile.objects.get(user=user)
        p_post = p.post_set.all()
        posts.append(p_post)

    my_posts = profile.profile_posts()
    posts.append(my_posts)
    if len(posts) > 0:
        posts = sorted(chain(*posts), reverse=True,
                       key=lambda obj: obj.date_posted)
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)
