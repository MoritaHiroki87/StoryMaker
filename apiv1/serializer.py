from rest_framework import serializers
from board.models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'project_name', )


class CurtainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtain
        fields = ('id', 'project', 'curtain_name',)


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'card_name', 'card_detail')
