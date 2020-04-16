from django.shortcuts import render, HttpResponseRedirect, reverse, Http404, HttpResponse
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView
from .models import *


# class IndexView(TemplateView):
#    template_name = 'index.html'

class SheetListView(ListView):
    template_name = 'ksheet/sheet_list.html'
    model = Sheet


class RecruitTemplateView(TemplateView):
    template_name = 'ksheet/recruit.html'


class SheetDetailView(DetailView):
    template_name = 'ksheet/detail.html'
    model = Sheet


class TrialSheetDetailView(DetailView):
    template_name = 'ksheet/trial_detail.html'
    model = Sheet

