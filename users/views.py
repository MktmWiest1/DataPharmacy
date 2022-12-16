from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User


def register_view(request):
    if request.method == "GET":
        return render(request, "register.html", context={
            "form": RegisterForm
        })
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('/')
        else:
            return render(request, "register.html", context={
                "form": RegisterForm
            })
def login_view(request):
    if request.method == "GET":
        return render(request, "login.html", context={
            "form": LoginForm
        })
    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password")
            )
        if user:
            login(request, user)
            return redirect('/')
    else:
        return render(request, "login.html", context={
            "form": LoginForm
        })  

def logout_view(request):
    logout(request)
    return redirect('/')