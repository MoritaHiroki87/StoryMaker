from django.urls import path, include
from .views import *


app_name = 'board'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<uuid:project_id>/', ProjectBoardView.as_view(), name='project_board'),
    path('<uuid:project_id>/new-curtain/', CreateCurtainView.as_view(), name='create_curtain'),
    path('<uuid:project_id>/<uuid:curtain_id>/', EditCurtainView.as_view(), name='edit_curtain'),
    path('<uuid:project_id>/<uuid:curtain_id>/delete/', DeleteCurtainView.as_view(), name='delete_curtain'),
    path('<uuid:project_id>/<uuid:curtain_id>/new-card/', CreateCardView.as_view(), name='create_card'),
    path('<uuid:project_id>/<uuid:curtain_id>/<uuid:card_id>/', EditCardView.as_view(), name='edit_card'),
    path('<uuid:project_id>/<uuid:curtain_id>/<uuid:card_id>/delete/', DeleteCardView.as_view(), name='delete_card'),
    # pdfの練習
    path('easypdf/', HelloPDFView.as_view(), name='easypdf'),
]

