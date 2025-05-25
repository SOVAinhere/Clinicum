from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.views import LoginView

from .forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

