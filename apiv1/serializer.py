from rest_framework import serializers
from board.models import *


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('card_name', 'card_detail')
