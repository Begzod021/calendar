from tkinter import CASCADE
from django.db import models



class StudentGroup(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()


class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    url = models.URLField()
    students = models.ForeignKey(StudentGroup, on_delete=models.PROTECT, null=True)

