from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)

class Student(models.Model):
    sname=models.CharField(max_length=100)
    sid=models.IntegerField(primary_key=True)
