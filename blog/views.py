from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Blog
from profiles.models import Profile


class PostList(LoginRequiredMixin, ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(blog=Blog.objects.get(owner=self.request.user))


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', ]
    success_url = '/posts/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.blog = Blog.objects.get(owner=user)
        return super().form_valid(form)


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post


class SubscriptionsList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/subscriptions_list.html'

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        subscriptions = profile.subscriptions.all()
        queryset = Post.objects.filter(blog__in=[blog for blog in subscriptions])

        return queryset


class BlogList(LoginRequiredMixin, ListView):
    model = Blog


class Login(LoginView):
    pass
