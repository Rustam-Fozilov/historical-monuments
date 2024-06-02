from django.contrib import admin

# Register your models here.
from .models import Cities
from unfold.admin import ModelAdmin


@admin.register(Cities)
class CitiesAdmin(ModelAdmin):
    list_display = ("name", "description", "image", "created_at")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    search_fields = ("name", "description", "image")

    class Meta:
        verbose_name = "Shaharlar"
        verbose_name_plural = "Shaharlar"
