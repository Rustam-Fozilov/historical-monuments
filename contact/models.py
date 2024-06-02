from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = 'Arizalar'
        verbose_name_plural = 'Arizalar'

    def __str__(self):
        return self.name
