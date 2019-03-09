from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    """カードのフォーム"""
    class Meta:
        model = Card
        fields = {
            'card_name',
            'card_detail',
            'card_order',
        }

