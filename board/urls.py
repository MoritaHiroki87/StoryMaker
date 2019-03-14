from django.urls import path
from . import views
from .views import *

app_name = 'board'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:project_id>/', ProjectView.as_view(), name='project'),
    path('<int:project_id>/new-curtain/', CreateCurtainView.as_view(), name='create_curtain'),
    path('<int:project_id>/<int:curtain_id/>', EditCurtainView.as_view(), name='edit_curtain'),
    # path('kaeseru/', views.kaeseru, name='kaeseru'),
    # path('permission/', views.permission_error, name='permission_error'),
]