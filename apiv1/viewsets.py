from board.models import Project, Card

import django_filters
from rest_framework import viewsets, filters
from .serializer import ProjectSerializer, CardSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer