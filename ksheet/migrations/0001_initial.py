# Generated by Django 2.1.7 on 2020-04-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, verbose_name='作品名')),
                ('author', models.CharField(max_length=32, verbose_name='作者')),
                ('course', models.CharField(choices=[('甘口', '甘口'), ('普通', '普通'), ('辛口', '辛口')], max_length=2)),
                ('page_count', models.IntegerField()),
                ('concept', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='コンセプト')),
                ('theme', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='テーマ')),
                ('story', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='ストーリー')),
                ('structure', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='構成')),
                ('character', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='キャラクター')),
                ('scene', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='シーン')),
                ('exposition', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='地の文')),
                ('dialogue', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='台詞')),
                ('total', models.IntegerField(choices=[(9, 'A+'), (8, 'A'), (7, 'A-'), (6, 'B+'), (5, 'B'), (4, 'B-'), (3, 'C+'), (2, 'C'), (1, 'C-')], default=5, verbose_name='総合評価')),
                ('concept_comment', models.TextField(blank=True, max_length=200)),
                ('theme_comment', models.TextField(blank=True, max_length=200)),
                ('story_comment', models.TextField(blank=True, max_length=200)),
                ('structure_comment', models.TextField(blank=True, max_length=200)),
                ('character_comment', models.TextField(blank=True, max_length=200)),
                ('scene_comment', models.TextField(blank=True, max_length=200)),
                ('exposition_comment', models.TextField(blank=True, max_length=200)),
                ('dialogue_comment', models.TextField(blank=True, max_length=200)),
                ('total_comment', models.TextField(blank=True, max_length=1000)),
                ('good_point', models.TextField(blank=True, max_length=1000)),
                ('bad_point', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
