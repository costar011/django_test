from django.contrib import admin
from . import models


@admin.register(models.DocBoardsModel)
class DocBoardAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "displayUser",
        "board_type",
        "created",
        "likeCount",
    )
    raw_id_fields = ("author",)
