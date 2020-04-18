from django.shortcuts import render, HttpResponseRedirect, reverse, Http404, HttpResponse
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# class IndexView(TemplateView):
#    template_name = 'index.html'

class SheetListView(ListView):
    template_name = 'ksheet/sheet_list.html'
    model = Sheet

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class RecruitTemplateView(TemplateView):
    template_name = 'ksheet/recruit.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SheetDetailView(DetailView):
    template_name = 'ksheet/detail.html'
    model = Sheet

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TrialSheetDetailView(DetailView):
    template_name = 'ksheet/trial_detail.html'
    model = Sheet

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

