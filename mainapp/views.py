from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *

from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.

        
class Home(View):
    def get(self, request):
        followers = ConnectPeople.objects.filter(person_who_follow = User.objects.get(username = request.user).id)
        blogs = Blogs.objects.filter(user__in = [i.person_to_be_followed for i in followers])
        print(blogs)
        if len(blogs) <= 10:
            pass
        else:
            blogs = blogs[:10]
        return render(request, 'mainapp/home.html', {'blogs': blogs})


class PostBlog(View):
    def get(self, request):
        return render(request, 'mainapp/postblog.html')
    def post(self, request):
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        blog = Blogs(title = title, image = image, content = content, user = User.objects.get(username = request.user))
        blog.save()
        # email_message = EmailMessage(
        #     self.sub,
        #     self.msg,
        #     settings.EMAIL_HOST_USER,
        #     self.stdsMails
        # )
        # email_message.fail_silently = True
        # email_message.send()
        return redirect('/mainapp/home')

class GetBlogs(View):
    def get(self, request):
        blogs = Blogs.objects.filter(user = User.objects.get(username = request.user))
        return render(request, 'mainapp/myblogs.html', {'blogs': blogs})

class ReadBlog(View):
    def get(self, request):
        uuid = request.GET['uuid']
        blog = Blogs.objects.get(uuid = uuid)
        likes = len(Likes.objects.filter(blog = blog))
        comments = Comments.objects.filter(blog = blog)
        return render(request, 'mainapp/readblog.html', {'blog': blog, 'likes': likes, 'comments': comments, 'commentlen': len(comments)})

class DeleteBlog(View):
    def get(self, request):
        uuid = request.GET['uuid']
        blog = Blogs.objects.get(uuid = uuid)
        blog.delete()
        return redirect('/mainapp/my-blogs')


class UpdateBlog(View):
    def get(self, request):
        uuid = request.GET['uuid']
        # blog = Blogs.objects.get(uuid = uuid)
        pass

class Profile(View):
    def get(self, request):
        user = User.objects.get(username = request.user)
        followers = ConnectPeople.objects.filter(person_to_be_followed = user)
        lst = []
        for i in followers:
            follower = User.objects.get(id = i.person_who_follow)
            lst.append(follower)
        return render(request, 'mainapp/profile.html', {'user': user, "followers": lst})


class SearchPage(View):
    def get(self, request):
        return render(request, 'mainapp/search.html', {'search': 'Search to get blogs you want'})

class SearchBlogs(View):
    def get(self, request):
        query_string = request.GET['query_string']
        blogs = Blogs.objects.filter(title__icontains = query_string)
        if len(blogs) != 0:
            return render(request, 'mainapp/search.html', {'blogs': blogs})
        else:
            return render(request, 'mainapp/search.html', {'search': 'No results found'})



class Follow(View):
    def get(self, request):
        followed_by = request.user
        person_to_be_followed = User.objects.get(username = request.GET['followed_to_be'])
        person_who_follow = User.objects.get(username = request.user).id
        check_query = ConnectPeople.objects.filter(person_to_be_followed = person_to_be_followed, person_who_follow = person_who_follow)
        if (str(followed_by) != str(request.GET['followed_to_be'])) and (len(check_query) == 0):
            conpeople = ConnectPeople(person_to_be_followed = person_to_be_followed, person_who_follow = person_who_follow)
            conpeople.save()
            return redirect('/mainapp/home')
        else:
            return redirect('/mainapp/home')


class Like(View):
    def get(self, request):
        uuid = request.GET['uuid']
        blog = Blogs.objects.get(uuid = uuid)
        user = User.objects.get(username = request.user)
        if len(Likes.objects.filter(blog = blog, user = user)) == 0:
            like = Likes(blog = blog, user = user)
            like.save()
            return redirect(f'/mainapp/read-blog?uuid={uuid}')
        else:
            Likes.objects.filter(blog = blog, user = user).delete()
            return redirect(f'/mainapp/read-blog?uuid={uuid}')

class Comment(View):
    def get(self, request):
        comment = request.GET['comment']
        uuid = request.GET['uuid']
        save_comment = Comments(
            user = User.objects.get(username = request.user),
            comment = comment,
            blog = Blogs.objects.get(uuid = uuid)
        )
        save_comment.save()
        return redirect(f'/mainapp/read-blog?uuid={uuid}')