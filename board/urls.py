from django.urls import path
from . import views
from .views import ProjectView

app_name = 'board'
urlpatterns = [
    # path('', views.index, name='index'),
    path('<int:project_id>/', ProjectView.as_view(), name='project'),
    # path('kaeseru/', views.kaeseru, name='kaeseru'),
    # path('permission/', views.permission_error, name='permission_error'),
]