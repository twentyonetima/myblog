from django.db import models

# Create your models here.


class About(models.Model):
    about_title = models.CharField('Name and last name', max_length=300)
    about_image = models.ImageField(upload_to='event_images/')
    about_text = models.TextField('Tell me abot you: ')

    def __str__(self):
        return self.about_title
