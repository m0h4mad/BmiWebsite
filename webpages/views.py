from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'webpages/index.html'


class AboutPageView(TemplateView):
    template_name = 'webpages/about.html'

