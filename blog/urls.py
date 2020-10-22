from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', SubscriptionsList.as_view(), name="subscriptions"),
    path('posts/', PostList.as_view(), name="user_posts"),
    path('post/<int:pk>/', PostDetail.as_view(), name="post"),
    path('post/create/', PostCreate.as_view(), name="post_create"),
    path('blogs/', BlogList.as_view(), name="blogs"),

    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]