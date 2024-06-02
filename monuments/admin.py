from django.contrib import admin

from monuments import models


# Register your models here.

@admin.register(models.Monument)
class MonumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    list_display_links = ('title',)
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    save_on_top = True
