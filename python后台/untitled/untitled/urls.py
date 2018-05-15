"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import xadmin,os
from untitled import settings
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from apps.users.views import LoginView,Dynamic_publishing,NewsView,Mobile,Square,Newspage

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',LoginView.as_view(),name="login"),
    path('captcha',include('captcha.urls')),
    path('dynamic_publishing', Dynamic_publishing.as_view(), name="dynamic_publishing"),
    path('news', NewsView.as_view(), name="news"),
    path('phone',Mobile.as_view(),name='mobile'),
    path('square',Square.as_view(),name='square'),
    path('newspage',Newspage.as_view(),name='newspage')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
