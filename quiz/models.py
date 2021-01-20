from django.db import models

# Create your models here.
class Quiz(models.Model):
    question=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    sol=models.CharField(max_length=100)
