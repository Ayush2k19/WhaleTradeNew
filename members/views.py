# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'RssFeed/register.html'
    success_url = reverse_lazy('login.html')


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'RssFeed/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
