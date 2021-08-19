import datetime

from django.db import models
from django.utils import timezone


class Film(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    image = models.ImageField()
    about = models.TextField()
    add_date = models.DateTimeField('дата загрузки: ')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.add_date <= now

