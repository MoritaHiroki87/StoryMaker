from .models import *


class CurtainViewModel(object):

    def __init__(self, curtain):
        self.curtain = curtain

    @property
    def order(self):
        return Curtain.objects.filter(project__id=self.curtain.project.id).count()

    def __getattr__(self, item):
        return getattr(self.curtain, item)


class CardViewModel(object):
    def __init__(self, card, length=100):
        self.card = card
        self.length = length

    """
    下記のように使う
    views.pyで
    card = Card.objects.get()
    card = CardViewModel(card, 100)
    
    templateで
    card.short_card_detail
    """
    @property
    def short_card_detail(self):
        return self.card_detail[:self.length]

    def __getattr__(self, item):
        return getattr(self.card, item)
