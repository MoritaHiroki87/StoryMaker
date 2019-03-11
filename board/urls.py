from django.urls import path
from . import views
from .views import *

app_name = 'board'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:project_id>/', ProjectView.as_view(), name='project'),
    path('project/<int:project_id>/new-curtain/', CurtainCreateView.as_view(), name='curtain_create')
    # path('kaeseru/', views.kaeseru, name='kaeseru'),
    # path('permission/', views.permission_error, name='permission_error'),
]