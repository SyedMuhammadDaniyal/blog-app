from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index", Home.as_view(), name= "index"),
    path("login", Login.as_view(), name= "login"),
    path("logout", login_required(Logout.as_view()), name= "logout"),
    path("signup", Signup.as_view(), name= "signup"),
    path("exception", exception.as_view(), name= "exception"),

]
