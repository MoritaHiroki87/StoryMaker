from board.models import Card

import django_filters
from rest_framework import viewsets, filters
from .serializer import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
