from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
# from django.views.generic import TemplateView, FormView, ListView
from .models import *
from .forms import *
from .services import get_card_list_as_json
from .view_models import *


# class IndexView(TemplateView):
#    template_name = 'index.html'
class ProjectListView(View):
    template_name = 'board/project_list.html'

    def get(self, request):
        projects = Project.objects.all()
        context = {'projects': projects}
        return render(request, self.template_name, context)


class ProjectView(View):
    """
    メインのボード画面。
    プロジェクトの情報、幕、カードそれぞれ必要。
    さらにプロジェクト切り替え、幕の作成・編集、カードの作成・編集へのリンクも必要。
    """
    template_name = 'board/project.html'

    def get(self, request, project_id):
        cards = get_card_list_as_json(project_id)
        project = Project.objects.filter(pk=project_id)

        context = {'cards': cards,
                   'project': project[0]}
        return render(request, self.template_name, context)


class CreateCurtainView(View):
    template_name = 'board/create_curtain.html'

    def get(self, request, project_id):
        create_curtain_form = CurtainForm
        context = {
            'create_curtain_form': create_curtain_form,
            'project_id': project_id,
        }
        return render(request, self.template_name, context)

    def post(self, request, project_id):
        create_curtain_form = CurtainForm(request.POST)
        if create_curtain_form.is_valid():
            create_curtain_form.save()
        return HttpResponseRedirect(reverse('board:create_curtain', args=(project_id,)))


class EditCurtainView(View):
    template_name = 'board/edit_curtain.html'

    def get(self, request, curtain_id):
        curtain = Curtain.objects.get(pk=curtain_id)
        curtain = CurtainViewModel(curtain)
        edit_curtain_form = CurtainForm(instnce=curtain)
        context = {
            'edit_curtain_form': edit_curtain_form
                   }
        return render(request, self.template_name, context)

    def post(self, request, curtain_id):
        curtain = Curtain.objects.get(pk=curtain_id)
        edit_curtain_form = CurtainForm(request.POST, instance=curtain)
        if edit_curtain_form.is_valid():
            edit_curtain_form.save()
        return HttpResponseRedirect(reverse('board:edit_curtain', args=(curtain_id,)))


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
