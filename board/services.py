from .models import *
from django.db.models import Q


def edit_curtain_order(obj, pre_order):
    """
    :param obj: ユーザーPOSTのデータ（編集後）
    :param pre_order: 編集前のorder
    :return: なし
    編集前後でorderを比較し、変更があれば処理。
    処理の内容は前後で大きくなった/小さくなったによって内容が変わる。
    また、今回変更したオブジェクトはここで追加で編集が起きないよう、クエリで弾く。
    """
    edited_order = obj.order
    pre_obj = obj.pk
    if edited_order < pre_order:
        # ここでCurtainOBJからオブジェクト生成してるけど、どうにかCardからも生成できないかな？
        curtains = Curtain.objects.filter(~Q(pk=pre_obj), order__gte=edited_order, order__lt=pre_order)
        for curtain in curtains:
            curtain.order += 1
            curtain.save()
    elif edited_order == pre_order:
        print('なし')
        return
    else:
        curtains = Curtain.objects.filter(~Q(pk=pre_obj), order__gt=pre_order, order__lte=edited_order)
        for curtain in curtains:
            curtain.order -= 1
            curtain.save()


def edit_card_order(obj, pre_order):
    """
    :param obj: ユーザーPOSTのデータ（編集後）
    :param pre_order: 編集前のorder
    :return: なし
    編集前後でorderを比較し、変更があれば処理。
    処理の内容は前後で大きくなった/小さくなったによって内容が変わる。
    また、今回変更したオブジェクトはここで追加で編集が起きないよう、クエリで弾く。
    """
    edited_order = obj.order
    pre_obj = obj.pk
    if edited_order < pre_order:
        # ここでCurtainOBJからオブジェクト生成してるけど、どうにかCardからも生成できないかな？
        curtains = Card.objects.filter(~Q(pk=pre_obj), order__gte=edited_order, order__lt=pre_order, curtain=obj.curtain)
        for curtain in curtains:
            curtain.order += 1
            curtain.save()
    elif edited_order == pre_order:
        print('なし')
        return
    else:
        curtains = Card.objects.filter(~Q(pk=pre_obj), order__gt=pre_order, order__lte=edited_order, curtain=obj.curtain)
        for curtain in curtains:
            curtain.order -= 1
            curtain.save()


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
    for curtain in Curtain.objects.filter(project=project).order_by('order', 'created_at'):
        curtain_dic = dict()
        curtain_dic["curtain_id"] = curtain.id
        curtain_dic["curtain_name"] = curtain.curtain_name

        card_list = []
        # cardが存在しないときどう動くのか心配
        for card in Card.objects.filter(curtain=curtain).order_by('order', 'created_at'):
            card_dic = dict()
            card_dic["card_id"] = card.id
            card_dic["order"] = card.order
            card_dic["card_name"] = card.card_name
            card_dic["card_detail"] = card.card_detail
            card_list.append(card_dic)

        curtain_dic["card_list"] = card_list
        curtain_list.append(curtain_dic)

    project_dic["curtain_list"] = curtain_list


    # print('-----project_dicの中身------')
    # print(project_dic)

    return project_dic
