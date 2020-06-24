from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageOrderView(TemplateView):
    template_name = 'orderMain.html'
    