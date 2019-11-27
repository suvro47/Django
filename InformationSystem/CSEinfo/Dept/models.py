from django.db import models
from django.conf import settings


class Student(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    Interest = models.TextField()

    def __str__(self):
        return self.Name


class Teacher(models.Model):
    Name = models.CharField(max_length=200)
    Dignity = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Research_Interest = models.TextField()

    def __str__(self):
        return self.Name


class Staff(models.Model):
    Name = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)

    def __str__(self):
        return self.Name
