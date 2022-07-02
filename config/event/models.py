from django.db import models
from students.models import StudentGroup

    

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    url = models.URLField()
    students = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    start_url = models.URLField(blank=True, null=True)
    join_url = models.URLField(blank=True, null=True)


