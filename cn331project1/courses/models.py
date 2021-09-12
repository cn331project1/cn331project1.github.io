from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.BooleanField()
    
    def __str__(self):
        return f"{self.code} {self.subject}"
