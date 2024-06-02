from django.db import models
import uuid
import os
# Create your models here.


def get_upload_path(instance, filename):
    unique_id = uuid.uuid4()
    ext = filename.split('.')[-1]
    new_filename = f"{unique_id}.{ext}"
    return os.path.join('cities/', new_filename)


class Cities(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
