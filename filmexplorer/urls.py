"""
URL configuration for filmexplorer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from films.views import film_list, film_list_template
from films.views import film_detail
from films.views import films04_db
from films.views import films05_with_links
from films.views import films06_datatable
from films import views
from films.views import signup

urlpatterns = [
    path('films01/', film_list, name='film_list'),
    path('films02/', film_list_template, name='film_list_template'),
    path('film_detail01/<str:title>/', film_detail, name='film_detail'),
    path('films04/', films04_db, name='films04_db'),
    path('films05/', films05_with_links, name='films05_with_links'),
    path('film/<slug:slug>/', film_detail, name='film_detail_slug'),
    path('films06/', films06_datatable, name='films06_datatable'),
    path('film/<slug:slug>/', views.film_detail, name='film_detail'),
    path('films07/', signup)
]
    