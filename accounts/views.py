from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect #added redirect
# from users.forms import CustomUserCreationForm #added this line
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

#
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


# def login(request):
#     return render(request, 'login.html')
#
#
# @login_required
# def index(request):
#     return render(request, 'index2.html')


# def register(request):
#     if request.method == "GET":
#         return render(
#             request, "users/register.html", {"form": CustomUserCreationForm}
#         )
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.backend = "django.contrib.auth.backends.ModelBackend"
#             user.save()
#             login(request, user)
#             return redirect(reverse("dashboard"))

