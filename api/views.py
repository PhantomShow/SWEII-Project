from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.

class HomePage(ListView):
    model = models.CustomUser
    template_name = 'index.html'
    context_object_name = 'user_list'

class UserDetail(DetailView):
    model = models.CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'user_detail'

    # Causing details to be empty for some reason ?
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UpdateUser(UpdateView):
    model = models.CustomUser
    form_class = forms.UserEditForm
    success_url = reverse_lazy('api:home_page')
    template_name = 'user_update.html'