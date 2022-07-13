from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import login_form, signup_form
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class login(LoginView):
    template_name = 'login.html'
    form_class = login_form


class logout(LogoutView):
    template_name = 'logout.html'


class signup(CreateView):
    model = User
    form_class = signup_form
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

