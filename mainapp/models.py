from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.
class Blogs(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(default="", max_length=100)
    image = models.ImageField(upload_to="media/blog/images")
    content = models.CharField(default="", max_length=5000)
    publish_date = models.DateTimeField(auto_now_add=True)
    
class ConnectPeople(models.Model):
    person_to_be_followed = models.ForeignKey(User, on_delete=models.CASCADE)
    person_who_follow = models.IntegerField(default=0)

class Likes(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(default="", max_length=1000)

# class Favourites(models.Model):
#     pass

