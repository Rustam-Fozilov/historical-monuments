from django.contrib import admin

from monuments import models


# Register your models here.

@admin.register(models.Monument)
class MonumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
