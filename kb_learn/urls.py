"""kb_learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from website import views
from website.views import *
from userregister import views as ac_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('adminoshsu1939/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cat/<int:pk>', cat, name='cat'),
    path('them/<int:pk>/<int:bi>', them_cat, name='them_cat'),
    path('post/<int:pk>', views.InfoView, name='post_detail'),
    path('info/', views.information, name='info'),
    path('programms/', views.program, name='programms'),
    path('register', ac_views.register, name='register'),
    path('login', ac_views.login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
