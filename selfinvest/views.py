from django.shortcuts import render
from django.views.generic import TemplateView

class page(TemplateView):
    template_name = 'temp.html'

class pageb(TemplateView):
    template_name = 'index.html'