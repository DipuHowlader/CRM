
from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model


class HomeView(generic.TemplateView):
    template_name = "home.html"


class SignupView(CreateView):
    template_name ='registration/signup.html' 
    form_class = UserCreationForm

    def get_success_url(self) :
        return reverse('login')
