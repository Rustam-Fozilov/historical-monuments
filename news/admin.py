from django.contrib import admin

from news.models import News
from unfold.admin import ModelAdmin


# Register your models here.


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    save_on_top = True
