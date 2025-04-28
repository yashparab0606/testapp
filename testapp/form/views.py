from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.views import welcome

# Home Page View
def home_view(request):
    return render(request, 'home/home.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('home') # redirect to home page
            return redirect('login')  # This will take the user to login page
    else:
            form = UserCreationForm()
    # return render(request, 'users/register.html',{'form':form})
    return render(request, "home/register.html", {"form": form})

    
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')  # <--- ✅ THIS SHOULD POINT TO Welcome page
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    # return render(request, 'users/login.html')
    return render(request, 'home/login.html')


def user_logout(request):
    logout(request)
    return redirect('home_view') # redirect to home page



