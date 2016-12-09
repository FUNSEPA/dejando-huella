""" auth URL Configuration
"""
from django.conf.urls import url
from apps.dh_auth import views

urlpatterns = [
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^signup/$', views.UserSignUp.as_view(), name='signup'), ]
