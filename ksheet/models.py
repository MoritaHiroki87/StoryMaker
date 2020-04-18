import uuid
from django.db import models
from django.utils import timezone
from  markdown import markdown
from users.models import User


# Create your models here.
class Sheet(models.Model):
    COURSE_LIST = (
        ("甘口", "甘口"),
        ("普通", "普通"),
        ("辛口", "辛口"),
    )
    ASSESSMENT_POINT_LIST = (
        (9, 'A+'), # プロでも見ない
        (8, 'A'), # プロ級
        (7, 'A-'), # うまい
        (6, 'B+'), # うまいが足りない
        (5, 'B'), # 普通に読める
        (4, 'B-'), # 普通に読めるが惜しい
        (3, 'C+'), # 初心者
        (2, 'C'), # 非の打ちどころしかない
        (1, 'C-'), # 非の打ちどころしかない
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 基本情報
    name = models.CharField(verbose_name="作品名", max_length=32)
    author = models.CharField(verbose_name="作者", max_length=32)
    appraiser = models.ForeignKey(User, verbose_name="評価者", on_delete=models.CASCADE)
    course = models.CharField(choices=COURSE_LIST, max_length=2)
    # 作品詳細情報
    page_count = models.IntegerField()
    # 評価項目 独創力、共感、印象が他にも。。
    concept = models.IntegerField(verbose_name="コンセプト", choices=ASSESSMENT_POINT_LIST, default=5) # 印象でもいいかも独創力もここでも。
    theme = models.IntegerField(verbose_name="テーマ", choices=ASSESSMENT_POINT_LIST, default=5) # これどうだろうな
    story = models.IntegerField(verbose_name="ストーリー", choices=ASSESSMENT_POINT_LIST, default=5) # 元は物語、共感？
    structure = models.IntegerField(verbose_name="構成", choices=ASSESSMENT_POINT_LIST, default=5)
    character = models.IntegerField(verbose_name="キャラクター", choices=ASSESSMENT_POINT_LIST, default=5)
    scene = models.IntegerField(verbose_name="シーン", choices=ASSESSMENT_POINT_LIST, default=5)
    exposition = models.IntegerField(verbose_name="地の文", choices=ASSESSMENT_POINT_LIST, default=5)
    dialogue = models.IntegerField(verbose_name="台詞", choices=ASSESSMENT_POINT_LIST, default=5)
    total = models.IntegerField(verbose_name="総合評価", choices=ASSESSMENT_POINT_LIST, default=5)
    # 詳細コメント
    concept_comment = models.TextField(blank=True, max_length=200) # 印象でもいいかも独創力もここでも。
    theme_comment = models.TextField(blank=True, max_length=200) # これどうだろうな
    story_comment = models.TextField(blank=True, max_length=200)
    structure_comment = models.TextField(blank=True, max_length=200)
    character_comment = models.TextField(blank=True, max_length=200)
    scene_comment = models.TextField(blank=True, max_length=200)
    exposition_comment = models.TextField(blank=True, max_length=200)
    dialogue_comment = models.TextField(blank=True, max_length=200)
    # 全体コメント
    total_comment = models.TextField(blank=True, max_length=1000)
    good_point = models.TextField(blank=True, max_length=1000)
    bad_point = models.TextField(blank=True, max_length=1000)

    # コメントのmarkdown化
    def concept_comment_as_md(self):
        """MarkDown記法で書かれたtextをHTML形式に変換して返す"""
        return markdown(self.concept_comment)

    def theme_comment_as_md(self):
        return markdown(self.theme_comment)

    def story_comment_as_md(self):
        return markdown(self.story_comment)

    def structure_comment_as_md(self):
        return markdown(self.structure_comment)

    def character_comment_as_md(self):
        return markdown(self.character_comment)

    def scene_comment_as_md(self):
        return markdown(self.scene_comment)

    def exposition_comment_as_md(self):
        return markdown(self.exposition_comment)

    def dialogue_comment_as_md(self):
        return markdown(self.dialogue_comment)

    def total_comment_as_md(self):
        return markdown(self.total_comment)

    def good_point_as_md(self):
        return markdown(self.good_point)

    def bad_point_as_md(self):
        return markdown(self.bad_point)





"""
    def __str__(self):
        return str(self.pattern_num)
"""
