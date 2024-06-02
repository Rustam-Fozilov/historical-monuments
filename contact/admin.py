from django.contrib import admin

# Register your models here.
from .models import Contact
from unfold.admin import ModelAdmin


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    list_filter = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone', 'message')

    class Meta:
        verbose_name = 'Arizalar'
        verbose_name_plural = 'Arizalar'