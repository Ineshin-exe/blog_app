from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post, Blog


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        return Post.objects.filter(blog=Blog.objects.get(author=self.request.user))


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'

    fields = ['title', 'content', ]
    success_url = '/posts/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.blog = Blog.objects.get(author=user)
        return super().form_valid(form)


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class SubscriptionsList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/subscriptions_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['read_posts'] = Post.objects.filter(readers=self.request.user)
        return context

    def get_queryset(self):
        user = self.request.user
        subscribed_blogs = Blog.objects.filter(subscribers=user)
        queryset = Post.objects.filter(blog__in=[blog for blog in subscribed_blogs])

        return queryset

    def post(self, request):
        user = self.request.user
        read_posts = Post.objects.filter(readers=user)

        post_id = request.POST.get("post_id")
        post = Post.objects.get(id=post_id)

        if post not in read_posts.all():
            post.readers.add(user)
            post.save()
        else:
            post.readers.remove(user)
            post.save()

        return redirect('/')


class BlogList(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscriptions_blogs'] = Blog.objects.filter(subscribers=self.request.user)
        return context

    def get_queryset(self):
        return Blog.objects.exclude(author=self.request.user)

    def post(self, request):
        user = self.request.user
        subscriptions_blogs = Blog.objects.filter(subscribers=user)

        blog_id = request.POST.get("blog_id")
        blog = Blog.objects.get(id=blog_id)

        blog_posts = Post.objects.filter(blog=blog)

        if blog not in subscriptions_blogs.all():
            blog.subscribers.add(user)
            blog.save()
        else:
            blog.subscribers.remove(user)
            for post in blog_posts:
                post.readers.remove(user)
                post.save()
            blog.save()

        return redirect('/blogs/')


class Login(LoginView):
    template_name = 'registration/login.html'


class Logout(LogoutView):
    template_name = 'registration/logout.html'


