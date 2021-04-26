from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render #redirect #added redirect
# from users.forms import CustomUserCreationForm #added this line


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

