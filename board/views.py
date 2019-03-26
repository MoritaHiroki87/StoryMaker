from django.shortcuts import render, HttpResponseRedirect, reverse, Http404
from django.views import View
# from django.views.generic import TemplateView, FormView, ListView
from .models import *
from .forms import *
from .services import *
from .view_models import *


# class IndexView(TemplateView):
#    template_name = 'index.html'

class ProjectListView(View):
    template_name = 'board/project_list.html'

    def get(self, request):
        # render関数は何を返しているのか？
        projects = Project.objects.all()
        context = {'projects': projects}
        return render(request, self.template_name, context)


class ProjectBoardView(View):
    """
    メインのボード画面。
    プロジェクトの情報、幕、カードそれぞれ必要。
    さらにプロジェクト切り替え、幕の作成・編集、カードの作成・編集へのリンクも必要。
    """
    template_name = 'board/project_board.html'

    def get(self, request, project_id):
        project = get_card_list_as_dict(project_id)
        context = {'project': project}
        return render(request, self.template_name, context)


class CreateCurtainView(View):
    template_name = 'board/create_curtain.html'

    def get(self, request, project_id):
        # form_view作った方がいいのかな？
        preset_project = Project.objects.get(pk=project_id)
        preset_order = Curtain.objects.filter(project=preset_project).count() + 1
        create_curtain_form = CurtainForm(initial={
            'project': preset_project,
            'order': preset_order,
        })
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

    def get(self, request, project_id, curtain_id):
        curtain = Curtain.objects.get(pk=curtain_id)
        # curtain = CurtainViewModel(curtain)
        edit_curtain_form = CurtainForm(instance=curtain)
        context = {
            'edit_curtain_form': edit_curtain_form,
            'project_id': project_id,
            "curtain_id": curtain_id,
                   }
        return render(request, self.template_name, context)

    def post(self, request, project_id, curtain_id):
        curtain = Curtain.objects.get(pk=curtain_id)
        edit_curtain_form = CurtainForm(request.POST, instance=curtain)
        pre_order = curtain.order
        if edit_curtain_form.is_valid():
            edit_curtain_order(curtain, pre_order)
            edit_curtain_form.save()
        return HttpResponseRedirect(reverse('board:edit_curtain', args=(project_id, curtain_id,)))


class DeleteCurtainView(View):

    def get(self, request, project_id, curtain_id):
        try:
            curtain = Curtain.objects.get(pk=curtain_id)
        except curtain.DoesNotExist:
            raise Http404

        curtain.delete()
        return HttpResponseRedirect(reverse('board:project_board', args=(project_id, )))


class CreateCardView(View):
    template_name = 'board/create_card.html'

    def get(self, request, project_id, curtain_id):
        preset_curtain = Curtain.objects.get(pk=curtain_id)
        preset_order = Card.objects.filter(curtain=preset_curtain).count() +1
        create_card_form = CardForm(initial={
            'curtain': preset_curtain,
            'order': preset_order,
        })
        context = {
            'create_card_form': create_card_form,
            'project_id': project_id,
            'curtain_id': curtain_id,
        }
        return render(request, self.template_name, context)

    def post(self, request, project_id, curtain_id):
        create_card_form = CardForm(request.POST)
        if create_card_form.is_valid():
            create_card_form.save()
        return HttpResponseRedirect(reverse('board:create_card', args=(project_id, curtain_id,)))


class EditCardView(View):
    template_name = 'board/edit_card.html'

    def get(self, request, project_id, curtain_id, card_id):
        card = Card.objects.get(pk=card_id)
        edit_card_form = CardForm(instance=card)
        context = {
            'edit_card_form': edit_card_form,
            'project_id': project_id,
            'curtain_id': curtain_id,
            'card_id': card_id,
                   }
        return render(request, self.template_name, context)

    def post(self, request, project_id, curtain_id, card_id):
        card = Card.objects.get(pk=card_id)
        edit_card_form = CardForm(request.POST, instance=card)
        pre_order = card.order
        if edit_card_form.is_valid():
            edit_card_order(card, pre_order)
            edit_card_form.save()
        return HttpResponseRedirect(reverse('board:edit_card', args=(project_id, curtain_id, card_id,)))


class DeleteCardView(View):
    def get(self, request, project_id, curtain_id, card_id):
        try:
            card = Card.objects.get(pk=card_id)
        except card.DoesNotExist:
            raise Http404

        card.delete()
        return HttpResponseRedirect(reverse('board:project_board', args=(project_id, )))


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
