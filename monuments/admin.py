from django.contrib import admin, messages

from monuments import models
from unfold.admin import ModelAdmin


# Register your models here.


@admin.register(models.Monument)
class MonumentAdmin(ModelAdmin):
    list_display = ('title', 'description_1', 'created_at')
    list_display_links = ('title',)
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    save_on_top = True
