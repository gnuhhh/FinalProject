from django.db import models

# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=1000000)
    answer1 = models.CharField(max_length=20)
    answer2 = models.CharField(max_length=20)
    answer3 = models.CharField(max_length=20)
    answer4 = models.CharField(max_length=20)
