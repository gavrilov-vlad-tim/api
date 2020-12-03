from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('success_signup')
    template_name = 'signup.html'


def success_signup(request):
    return render(request, 'success-signup.html')
