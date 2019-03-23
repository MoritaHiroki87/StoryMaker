from .models import *
from collections import OrderedDict


def get_card_list_as_dict(project_id):
    """
    :param project_id: プロジェクトのid
    :return: json（OrderedDict）
    {
     "project_id": 1,
     "project_name": "project_1",
     "curtain": [{
        "curtain_id": 1,
        "curtain_name": "curtain_1",
        "card": [{
            "card_id": 1,
            "card_name": "card_1",
            "card_detail": "detail"
            },
            {
            "card_id": 2,
            "card_name": "card_2",
            "card_detail": "detail"
            },
            ...
            ]
        },
        {
        "curtain_id": 2,
        "curtain_name": "curtain_2",
        "card": [{
            "card_id": 1,
            "card_name": "card_1",
            "card_detail": "detail"
            },
            {
            "card_id": 2,
            "card_name": "card_2",
            "card_detail": "detail"
            },
            ...
            ]
        }
        ]
    }
    的なやつ
    """
    project = Project.objects.get(pk=project_id)

    project_dic = dict()
    project_dic["project_id"] = project_id
    project_dic["project_name"] = project.project_name

    curtain_list = []
    for curtain in Curtain.objects.filter(project=project).order_by('order', 'pk'):
        curtain_dic = dict()
        curtain_dic["curtain_id"] = curtain.pk
        curtain_dic["curtain_name"] = curtain.curtain_name

        card_list = []
        # cardが存在しないときどう動くのか心配
        for card in Card.objects.filter(curtain=curtain).order_by('card_order', 'pk'):
            card_dic = dict()
            card_dic["card_order"] = card.card_order
            card_dic["card_name"] = card.card_name
            card_dic["card_detail"] = card.card_detail
            card_list.append(card_dic)

        curtain_dic["card_list"] = card_list
        curtain_list.append(curtain_dic)

    project_dic["curtain_list"] = curtain_list

    """
    cards = Card.objects.filter(curtain__project=project_id).order_by('curtain', 'card_order')
    curtains = Curtain.objects.filter(project=project_id)

    card_list = {}
    card_list_per_curtain = []
    curtain_st = cards[0].curtain

    for card in cards:
        # print(card.card_name, card.curtain.curtain_name, card.card_order)
        if curtain_st != card.curtain:
            ""
            curtain_idが切り替わったら、
            card_listに{curtain_st: card_list_per_curtain}を入れ、
            cutain_stは新しいものに切り替え、
            card_list_per_curtainは空白にする。
            んで、if文抜けたところでcard_list_per_curtainは
            どんどん追加してる
            ""
            # print('curtainの切り替え: ', curtain_st.curtain_name, '=>', card.curtain.curtain_name)
            card_list[curtain_st] = card_list_per_curtain
            curtain_st = card.curtain
            card_list_per_curtain = []
        card_list_per_curtain.append(card)
    card_list[curtain_st] = card_list_per_curtain

    # print('色々やる前のcard_listのキー:', card_list.keys())

    for curtain in curtains:
        if curtain not in card_list.keys():
            card_list[curtain] = []
    """

    print('-----project_dicの中身------')
    print(project_dic)

    return project_dic
