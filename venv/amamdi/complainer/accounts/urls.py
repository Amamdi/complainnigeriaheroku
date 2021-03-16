from .views import SignUpView
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
