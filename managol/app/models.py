from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        ('1', 'ROOT'),
        ('2', 'DG'),
        ('3', 'DE'),
        ('4', 'COM'),
        ('5', 'PROF'),
    )

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class SessionYear(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + " - " + self.session_end


class Classe(models.Model):
    LEVEL = (
        ('maternelle', 'Maternelle'),
        ('primaire', 'Primaire'),
        ('college', 'College'),
        ('lycee', 'Lycee'),
    )
    name = models.CharField(max_length=100)
    level = models.CharField(choices=LEVEL, max_length=50)
    total = models.IntegerField()
    cost = models.FloatField()
    session_id = models.ForeignKey(SessionYear, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    classe_id = models.ForeignKey(Classe, on_delete=models.DO_NOTHING)
    date_join = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    address = models.TextField()
    picture = models.ImageField(upload_to='media/student_pic')
    session_id = models.ForeignKey(SessionYear, on_delete=models.DO_NOTHING)
    father_name = models.CharField(max_length=100)
    father_profession = models.CharField(max_length=100)
    father_phone = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_profession = models.CharField(max_length=100)
    mother_phone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    courses = models.CharField(max_length=100)
    date_join = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    address = models.TextField()
    picture = models.ImageField(upload_to='media/prof_pic')
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    prof_id = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
