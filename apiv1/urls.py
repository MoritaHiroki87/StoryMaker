from django.urls import include, path
from rest_framework import routers
from . import viewsets


project_router = routers.DefaultRouter()
project_router.register('projects', viewsets.ProjectViewSet)

curtain_router = routers.DefaultRouter()
curtain_router.register('curtains', viewsets.CurtainViewSet)

card_router = routers.DefaultRouter()
card_router.register('cards', viewsets.CardViewSet)

urlpatterns = [
    path('', include(project_router.urls)),
    path('', include(curtain_router.urls)),
    path('', include(card_router.urls)),
]

