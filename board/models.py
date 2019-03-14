from django.db import models


# Create your models here.
class Project(models.Model):
    """
    プロジェクト
    project_name:プロジェクト名
    created_at:作成日時
    updated_at:更新日時
    """
    """
    class Meta:
        db_table = "project"
    """
    project_name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

"""
    def __str__(self):
        return str(self.pattern_num)
"""


class Curtain(models.Model):
    """
    幕
    project:プロジェクト
    curtain_name:幕名
    """
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    curtain_name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # order = models.IntegerField(default=)


class Card(models.Model):
    """
    カード
    curtain:幕
    card_mane:カード名
    card_detail:カード詳細
    created_at:作成日時
    updated_at:更新日時
    """
    curtain = models.ForeignKey(Curtain, null=True, blank=True, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=32)
    card_detail = models.TextField()
    card_order = models.IntegerField(default=1)
    # card_order = models.IntegerField(default=lambda: Card.objects.last('pk').pk + 1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


