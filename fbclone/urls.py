"""fbclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
# from myapp.views import UserViewSet
from api.views import UserViewSet,ClassStudentView
from rest_framework.routers import DefaultRouter

from rest_framework import routers
router = DefaultRouter()
router.register('studentapi', UserViewSet, basename='Student')
router.register('studentclass', ClassStudentView, basename='StudentClass')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('l',include('login.urls')),
    path('',include(router.urls)),
    path('auths/',include('rest_framework.urls',namespace='rest_framework')),
    path('api/',include('api.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

