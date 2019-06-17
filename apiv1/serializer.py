from rest_framework import serializers
from board.models import *


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'card_name', 'curtain', 'card_detail',)


class CurtainSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Curtain
        fields = ('id', 'curtain_name', 'project', 'cards')


class ProjectSerializer(serializers.ModelSerializer):
    curtains = CurtainSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'curtains')
