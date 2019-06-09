from django.urls import path, include
from .views import *


app_name = 'board'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<str:project_id>/', ProjectBoardView.as_view(), name='project_board'),
    path('<str:project_id>/new-curtain/', CreateCurtainView.as_view(), name='create_curtain'),
    path('<str:project_id>/<str:curtain_id>/', EditCurtainView.as_view(), name='edit_curtain'),
    path('<str:project_id>/<str:curtain_id>/delete/', DeleteCurtainView.as_view(), name='delete_curtain'),
    path('<str:project_id>/<str:curtain_id>/new-card/', CreateCardView.as_view(), name='create_card'),
    path('<str:project_id>/<str:curtain_id>/<str:card_id>/', EditCardView.as_view(), name='edit_card'),
    path('<str:project_id>/<str:curtain_id>/<str:card_id>/delete/', DeleteCardView.as_view(), name='delete_card'),
    # pdfの練習
    path('easypdf/', HelloPDFView.as_view(), name='easypdf'),
]

