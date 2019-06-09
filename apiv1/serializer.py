from rest_framework import serializers
from board.models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name', )


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('card_name', 'card_detail')
