from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)