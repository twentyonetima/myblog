from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        return self.text[:50]

    class Meta:
        verbose_name = 'Post in blog'
        verbose_name_plural = 'Posts in blog'

    def __str__(self):
        return self.title
