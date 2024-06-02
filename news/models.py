import uuid
import os

from django.db import models

# Create your models here.


def get_upload_path(instance, filename):
    unique_id = uuid.uuid4()
    ext = filename.split('.')[-1]
    new_filename = f"{unique_id}.{ext}"
    return os.path.join('news/', new_filename)


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Yangiliklar'
        verbose_name_plural = 'Yangiliklar'

    def __str__(self):
        return self.title
