from django.shortcuts import render
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = "home.html"

class Project(TemplateView):
    template_name = "project.html"