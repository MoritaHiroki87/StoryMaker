from .models import *


def get_card_list_as_json(project_id):
    cards = Card.objects.filter(curtain__project=project_id).order_by('curtain', 'card_order')

    card_list = {}
    card_list_per_curtain = []
    curtain_st = cards[0].curtain
    for card in cards:
        print(card.card_name, card.curtain.curtain_name, card.card_order)
        if curtain_st != card.curtain:
            """
            curtain_idが切り替わったら、
            card_listに{curtain_st: card_list_per_curtain}を入れ、
            cutain_stは新しいものに切り替え、
            card_list_per_curtainは空白にする。
            んで、if文抜けたところでcard_list_per_curtainは
            どんどん追加してる
            """
            print('curtainの切り替え: ', curtain_st.curtain_name, '=>', card.curtain.curtain_name)
            card_list[curtain_st] = card_list_per_curtain
            curtain_st = card.curtain
            card_list_per_curtain = []
        card_list_per_curtain.append(card)
    card_list[curtain_st] = card_list_per_curtain

    return card_list
