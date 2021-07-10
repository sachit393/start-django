from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default='')
    password = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200, default='')
    college = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=30, default='')
    #filters preferences
    cgpa = models.DecimalField(decimal_places=2,max_digits=5)
    description = models.TextField(blank=True)
    cv = models.URLField(null=True)

    def __str__(self):
        return self.name


class Organizer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    contact = models.URLField(blank=True)

    def __str__(self):
        return self.name
