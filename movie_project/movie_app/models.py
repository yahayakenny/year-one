from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50, blank = True, null = True)
    thumbs_up = models.PositiveIntegerField(default = 0)
    thumbs_down = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title




