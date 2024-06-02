from django.contrib import admin

from news.models import News


# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    save_on_top = True
