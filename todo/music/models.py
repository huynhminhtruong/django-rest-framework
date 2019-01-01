from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]
