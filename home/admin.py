from django.contrib import admin

from home.models import Favorite
from unfold.admin import ModelAdmin
# Register your models here.


@admin.register(Favorite)
class FavoriteAdmin(ModelAdmin):
    list_display = ('user', 'monument')
    list_filter = ('user', 'monument')
    search_fields = ('user', 'monument')

