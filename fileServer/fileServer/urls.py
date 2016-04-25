"""fileServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
   url(r'^login/', 'fileServer.views.loginView'),
   url(r'^auth/', 'fileServer.views.authLogin'),
   url(r'^logout/', 'fileServer.views.authLogout'),
   url(r'^signup/', 'fileServer.views.authSignup'),
   url(r'^uploadFile/', 'fileServer.views.managerView'),
   url(r'^$', 'fileServer.views.managerView'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
