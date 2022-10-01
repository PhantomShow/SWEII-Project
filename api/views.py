from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from . import forms
from django.contrib import auth
# Create your views here.

class HomePage(ListView):
    model = auth.models.User
    template_name = 'index.html'

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'