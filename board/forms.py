from django import forms
from .models import *


class CardForm(forms.ModelForm):
    """カードのフォーム"""
    class Meta:
        model = Card
        fields = {
            'card_name',
            'card_detail',
            'card_order',
        }


class CurtainForm(forms.ModelForm):

    class Meta:
        model = Curtain
        fields = {
            'project',
            'curtain_name',
        }


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = {
            'project_name',
        }
