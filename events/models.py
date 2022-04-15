from django.db import models


class Event(models.Model):
    event_image = models.ImageField(upload_to='event_images/')
    event_text = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Post in event'
        verbose_name_plural = 'Posts in event'

    def __str__(self):
        return self.event_text
