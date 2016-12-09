from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'home.html'


class HistoriaView(TemplateView):
	template_name = 'blog/historia.html'
