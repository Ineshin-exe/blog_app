from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView

from blog.forms import FollowForm
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

    def post(self, request):
        user = self.request.user
        profile = Profile.objects.get(user=user)

        post_id = request.POST.get("post_id")

        print(post_id)

        if Post.objects.get(id=post_id) not in profile.read.all():
            profile.read.add(Post.objects.get(id=post_id))
            profile.save()
        else:
            profile.read.remove(Post.objects.get(id=post_id))
            profile.save()

        return redirect('/')


class BlogList(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.exclude(owner=self.request.user)

    def post(self, request):
        user = self.request.user
        profile = Profile.objects.get(user=user)

        blog_id = request.POST.get("blog_id")

        if Blog.objects.get(id=blog_id) not in profile.subscriptions.all():
            profile.subscriptions.add(Blog.objects.get(id=blog_id))
            profile.save()
        else:
            profile.subscriptions.remove(Blog.objects.get(id=blog_id))
            profile.save()

        return redirect('/blogs/')


class SubscribeForm(LoginRequiredMixin, FormView):
    form_class = FollowForm
    template_name = "blog/subscribe_form.html"


class Login(LoginView):
    pass


class Logout(LogoutView):
    template_name = 'registration/logout.html'


