from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import UserManager,PermissionsMixin,AbstractBaseUser
from django.db import models

# Create your models here.

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, default='',unique=True)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    # qualification = models.CharField(max_length=200, default='')
    college = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=30, default='')
    # filters preferences
    cgpa = models.DecimalField(decimal_places=2, max_digits=5,null=True)
    description = models.TextField(blank=True)
    cv = models.URLField(null=True)
    skills = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=200, null=True)
    year = models.IntegerField(null=True)
    # following_companies = models.ManyToManyField()
    # jobs_applied = models.ManyToManyField(Jobs)
    # work_place_preferred = models.CharField(null=True)
    degree = models.CharField(max_length=200, null=True)
    is_staff = models.BooleanField(default=False)
    last_login = timezone.now()

    # objec

    def __str__(self):
        return self.username


class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    contact = models.URLField(blank=True)


    def __str__(self):
        return self.username
