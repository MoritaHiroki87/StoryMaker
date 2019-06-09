from django.urls import include, path
from rest_framework import routers
from . import viewsets


router = routers.DefaultRouter()
router.register('cards', viewsets.CardViewSet)

urlpatterns = [
    path('', include(router.urls))
]

