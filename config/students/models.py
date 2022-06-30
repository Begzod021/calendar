from django.db import models

# Create your models here.
class StudentGroup(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    student_group = models.IntegerField(null=True)