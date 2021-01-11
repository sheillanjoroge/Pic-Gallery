"""Galleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from photos.views import index, show_image, search, discover, images_by_tag, images_by_location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('photo/<int:id>', show_image, name='show_image'),
    path('search', search, name='search'),
    path('discover', discover, name='discover'),
    path('tag/<int:id>', images_by_tag, name='images_by_tag'),
    path('location/<int:id>', images_by_location, name='images_by_tag')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)