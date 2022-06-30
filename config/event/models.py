from django.db import models
from students.models import StudentGroup

    

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    url = models.URLField()
    students = models.ForeignKey(StudentGroup, on_delete=models.PROTECT)


