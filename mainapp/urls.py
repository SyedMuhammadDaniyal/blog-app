from os import name
from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home.as_view(), name="home page"),
    path('post-blog/', PostBlog.as_view(), name = "post blog"),
    path('my-blogs/', GetBlogs.as_view(), name = "my blogs"),
    re_path(r'^read-blog/$', ReadBlog.as_view(), name="read blog"),
    re_path(r'^delete-blog/$', DeleteBlog.as_view(), name="Delete blog"),
    re_path(r'^update-blog/$', UpdateBlog.as_view(), name="Update blog"),
    path('profile/', Profile.as_view(), name="Profile"),
    re_path(r'^search/$', SearchBlogs.as_view(), name = 'Search Blogs'),
    path('search-blogs', SearchPage.as_view(), name='search page'),
    re_path(r'^follow/$', Follow.as_view(), name='follow api'),
    re_path(r'^like/$', Like.as_view(), name = 'Like'),
    re_path(r'^comment/$', Comment.as_view(), name = 'Comment'),
]