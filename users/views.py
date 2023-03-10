from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms, models


class RegisterView(CreateView):
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = "/users/"


class NewLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "login.html"
    success_url = "/users/"


class UserListView(ListView):
    template_name = "users.html"
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset
