from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'comprado', 'criado_em')
    list_filter = ('comprado', 'criado_em')
    search_fields = ('nome',)
