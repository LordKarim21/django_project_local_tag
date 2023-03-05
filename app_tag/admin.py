from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_display_links = ['name', ]
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}
