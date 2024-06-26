import uuid
import os

from django.db import models
from django.conf import settings

# Create your models here.


def get_upload_path(instance, filename):
    unique_id = uuid.uuid4()
    ext = filename.split('.')[-1]
    new_filename = f"{unique_id}.{ext}"
    return os.path.join('monuments/', new_filename)


class Monument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description_1 = models.TextField(blank=True, null=True)
    description_2 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_path)
    video = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Obida'
        verbose_name_plural = 'Obidalar'

    def __str__(self):
        return self.title
