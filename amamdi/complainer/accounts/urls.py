from .views import SignUpView #register
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('oauth/', include('social_django.urls', namespace='social:begin')),
    # path('register/', register, name='register')
]
