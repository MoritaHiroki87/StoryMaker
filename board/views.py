from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
# from django.views.generic import TemplateView, FormView, ListView
from .models import *
from .forms import *
from .services import get_card_list_as_json


# class IndexView(TemplateView):
#    template_name = 'index.html'
class ProjectListView(View):
    template_name = 'board/project_list.html'

    def get(self, request):
        projects = Project.objects.all()
        context = {'projects': projects}
        return render(request, self.template_name, context)


class ProjectView(View):
    template_name = 'board/project.html'

    def get(self, request, project_id):
        cards = get_card_list_as_json(project_id)
        print(cards)
        project = Project.objects.filter(pk=project_id)

        context = {'cards': cards,
                   'project': project[0]}
        return render(request, self.template_name, context)


class CurtainCreateView(View):
    template_name = 'board/curtain_create.html'

    def get(self, request, project_id):
        curtain_create_form = CurtainForm
        context = {
            'curtain_create_form': curtain_create_form,
            'project_id': project_id,
        }
        return render(request, self.template_name, context)

    def post(self, request, project_id):
        curtain_create_form = CurtainForm(request.POST)
        curtain_create_form.save()
        return HttpResponseRedirect(reverse('board:curtain_create', args=(project_id,)))


class CurtainEditView(View):
    template_name = 'board/curtain_edit.html'

    def get(self, request, curtain_id):
        curtain = Curtain.objects.filter(pk=curtain_id)




"""
class DashboardView(ListView):
    model = Card
    # paginate_ by = 5
    template_name = "board/dashboard.html"

    def get_queryset(self):
        cards = Card.objects.select_related().filter(Curtain_id = 1).all()
        project = Project.objects.filter(pk=1)
        context = {}

    def form_valid(self, form):

        context = {
            "form": form,
        }

        return render(self.request, "board/dashboard.html", context)


class RentMinView(FormView):
    template_name = 'rentvalue/rentmin.html'
    form_class = RentMinForm

    def form_valid(self, form):
        postal_num = form.cleaned_data["postal_num"]
        tmp = postalSearch(postal_num)
        context = {
            "form": form,
            "rent_min": tmp[1],
        }
        return render(self.request, 'rentvalue/rentmin.html', context)
"""
