from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username ,first_name=firstname, last_name=lastname, email=email, password=password)
        user.save()
        print('user created')
        return redirect('login')
    else:
        return render(request,'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')    
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


