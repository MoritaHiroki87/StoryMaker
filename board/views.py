from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView, ListView
from .models import Project, Curtain, Card



#class IndexView(TemplateView):
#    template_name = 'index.html'

class ProjectView(View):
    template_name = 'board/project.html'

    def get(self, request, project_id):
        project = Project.objects.filter(pk=project_id)
        cards = Card.objects.all()
        context = {'cards': cards,
                   'project_name': project.project_name}
        return render(request, self.template_name, context)


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
