from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'authentication/index.html')

class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request, username = username, password = password)
        if auth is not None:
            login(request, auth)

        else:
            return HttpResponse("<h1>400 BAD REQUEST</h1>")
        return redirect('/mainapp/home')

class Logout(View):
    def get(self, request):
        print(request.user)
        logout(request)
        return redirect('/auth/index')

class Signup(View):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        auth = authenticate(request, username = username, password = password)
        if auth is not None:
            login(request, auth)
        else:
            return HttpResponse("<h1>400 BAD REQUEST</h1>")
        return redirect('/mainapp/home')



class exception(View):
    def get(self, request):
        return HttpResponse("404")