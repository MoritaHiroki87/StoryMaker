from django.urls import path
from . import views
from .views import *

app_name = 'board'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:project_id>/', ProjectBoardView.as_view(), name='project_board'),
    path('<int:project_id>/new-curtain/', CreateCurtainView.as_view(), name='create_curtain'),
    path('<int:project_id>/<int:curtain_id>/', EditCurtainView.as_view(), name='edit_curtain'),
    path('<int:project_id>/<int:curtain_id>/delete/', DeleteCurtainView.as_view(), name='delete_curtain'),
    path('<int:project_id>/<int:curtain_id>/new-card/', CreateCardView.as_view(), name='create_card'),
    path('<int:project_id>/<int:curtain_id>/<int:card_id>/', EditCardView.as_view(), name='edit_card'),
    path('<int:project_id>/<int:curtain_id>/<int:card_id>/delete/', DeleteCardView.as_view(), name='delete_card'),
    # pdfの練習
    path('print/', MyModelPrintView.as_view(), name='project_list_pdf'),
]