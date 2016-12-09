""" voluntariado URL Configuration
"""
from django.conf.urls import url
from apps.voluntariado import views

urlpatterns = [
    url(r'^$', views.HistoriaView.as_view(), name='historia'), ]
