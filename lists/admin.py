from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin Definitio """

    pass
