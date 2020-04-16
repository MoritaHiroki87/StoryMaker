from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Sheet)
class SheetAdmin(admin.ModelAdmin):
    list_display = ["name", "author",]
    list_display_links = ["name", ]
    fields = ("name", "author", "course", "page_count",
              ("concept", "concept_comment"),
              ("theme", "theme_comment"),
              ("story", "story_comment"),
              ("structure", "structure_comment"),
              ("character", "character_comment"),
              ("scene", "scene_comment"),
              ("exposition", "exposition_comment"),
              ("dialogue", "dialogue_comment"),
              ("total", "total_comment"),
              "good_point", "bad_point",
              )