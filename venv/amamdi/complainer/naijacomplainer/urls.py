from django.urls import path  
from naijacomplainer import views as response_views
from .views import (searchposts)


app_name = "naijacomplainer"
urlpatterns = [
    path('', response_views.base),
    path('index/', response_views.emp),
    path('dashboard/', response_views.dashboard),
    path('search/', searchposts, name='searchposts'),

      
]
