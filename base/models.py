from django.db import models

# Create your models here.

class Student(models.Model):
    Gender=[
        ('Male','Male'),('Female','Female'),('Other','Other')
    ]
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100,choices=Gender)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    mock=models.BooleanField()
    
    def __str__(self):
        return self.name
    