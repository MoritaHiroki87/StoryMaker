from django.urls import include, path
from rest_framework import routers
from . import viewsets


card_router = routers.DefaultRouter()
card_router.register('cards', viewsets.CardViewSet)

project_router = routers.DefaultRouter()
project_router.register('projects', viewsets.ProjectViewSet)

urlpatterns = [
    path('', include(card_router.urls)),
    path('', include(project_router.urls))
]

