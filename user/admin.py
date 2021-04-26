from django.contrib import admin
from . import models


@admin.register(models.UsersModel)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "displayUser",
    )
    raw_id_fields = ("author",)