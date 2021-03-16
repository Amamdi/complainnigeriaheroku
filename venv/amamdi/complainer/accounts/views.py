from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# def login(request):
#     return render(request, 'login.html')
#
#
# @login_required
# def index(request):
#     return render(request, 'index.html')


