from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class AdminDashBoardView(TemplateView):
    template_name = "dashboard.html"