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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from naijacomplainer import views
from django.conf.urls.static import static
from django.conf import settings
# from accounts import views as account_views
from naijacomplainer.views import HomeView, get_data, ChartData, ChartData2, ChartData3, PieChartView, AreaChartView, BarChartView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('emp', views.emp, name="index2"),
    path('login/login/accounts/', include('accounts.urls')),
    path('login/login/accounts/', include('django.contrib.auth.urls')),
    path('login/', include('django.contrib.auth.urls')),
    # path('oauth/', include('social_django.urls')),
    path('login/', include('social_django.urls')),
    # path('login/login/accounts/', include('social_django.urls')),
    # path('login/login/accounts/oauth/', include('accounts.urls')),
    path('index2/', views.emp, name="index2"),
    # path('dashboard/', views.dashboard),
    path('success/', views.success, name='success'),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.destroy, name="delete"),
    path('search/', include('naijacomplainer.urls'), name="search"),
    # path('success/chart/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path('success/chart/', HomeView.as_view(), name='chart'),
    path("pie/", csrf_exempt(PieChartView.as_view()), name="pie_chart"),
    path("area/", AreaChartView.as_view(), name="area_chart"),
    path("bar/", BarChartView.as_view(), name="bar_chart"),
    # path, ('success/chart/complaints/<int:year>/', views.get_complaints_chart, name='chart-complaints'),
    path('api/data/', get_data, name='api-data'),
    path('api/chart/data', ChartData.as_view(), name='chartdata'),
    path('api/chart2/data2', ChartData2.as_view(), name='chartdata2'),
    path('api/chart3/data3', ChartData3.as_view(), name='chartdata3'),
    # path('map/', views.map, name='map'),
    # path("search/", include("naijacomplainer.urls"), namespace=)
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
