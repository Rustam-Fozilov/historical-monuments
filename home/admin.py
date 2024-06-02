from django.contrib import admin

from home.models import Favorite
# Register your models here.


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'monument')
    list_filter = ('user', 'monument')
    search_fields = ('user', 'monument')

