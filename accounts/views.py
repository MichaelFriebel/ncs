from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .forms import (
    CustomUserCreationForm, 
    )

class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")
