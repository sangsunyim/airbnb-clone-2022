from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdin(admin.ModelAdmin):

    pass