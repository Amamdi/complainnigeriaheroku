"""complainer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  
from django.urls import path, include
from naijacomplainer import views
from django.conf.urls.static import static
from django.conf import settings
from naijacomplainer.views import HomeView, get_data, ChartData, ChartData2, ChartData3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base),
    path('emp', views.emp, name="index"),
    path('login/login/accounts/', include('accounts.urls')),
    path('login/login/accounts/', include('django.contrib.auth.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('index/', views.emp, name="index2"),
    # path('dashboard/', views.dashboard),
    path('success/', views.success, name='success'),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.destroy, name="delete"),
    path('search/', include('naijacomplainer.urls'), name="search"),
    path('success/chart/', HomeView.as_view(), name='chart'),
    path('api/data/', get_data, name='api-data'),
    path('api/chart/data', ChartData.as_view(), name='chartdata'),
    path('api/chart2/data2', ChartData2.as_view(), name='chartdata2'),
    path('api/chart3/data3', ChartData3.as_view(), name='chartdata3')
    # path("search/", include("naijacomplainer.urls"), namespace=)
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
