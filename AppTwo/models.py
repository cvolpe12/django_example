from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.CharField(max_length=264, unique=True)
    # this can be EmailField

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class School(models.Model):
    name = models.CharField(max_length=264)
    principal = models.CharField(max_length=264)
    location = models.CharField(max_length=264)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
