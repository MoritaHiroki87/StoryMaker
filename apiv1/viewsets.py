from board.models import Project, Curtain, Card
from rest_framework import viewsets
from .serializer import ProjectSerializer, CurtainSerializer, CardSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CurtainViewSet(viewsets.ModelViewSet):
    queryset = Curtain.objects.all()
    serializer_class = CurtainSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
