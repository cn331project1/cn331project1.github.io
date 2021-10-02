from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CourseModel(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.BooleanField()
    student = models.ManyToManyField(User, blank = True, related_name = "students")

    def __str__(self):
        return f"{self.code} {self.name}"
