from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', SubscriptionsList.as_view()),
    path('posts/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('post/create/', PostCreate.as_view()),
    path('blogs/', BlogList.as_view()),
    path('subscribe/', SubscribeForm.as_view()),

    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
]