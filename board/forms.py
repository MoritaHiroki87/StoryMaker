from django import forms
from .models import *


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = {
            'project_name',
        }


class CurtainForm(forms.ModelForm):

    class Meta:
        model = Curtain
        fields = (
            'curtain_name',
        )


class EditCurtainForm(CurtainForm):
    class Meta:
        model = Curtain
        fields = (
            'curtain_name',
            'order',
        )


class CardForm(forms.ModelForm):
    """カードのフォーム"""
    class Meta:
        model = Card
        fields = {
            'card_name',
            'card_detail',
        }


class EditCardForm(CardForm):
    """カードのフォーム"""
    field_order = ['card_name', 'card_detail', 'order', ]

    class Meta:
        model = Card
        fields = {
            'card_name',
            'card_detail',
            'order',
        }