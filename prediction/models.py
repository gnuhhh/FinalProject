# prediction/models.py
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class MajorGroup(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    major_group = models.ForeignKey(MajorGroup, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['code', 'university']
    
    def __str__(self):
        return f"{self.name} - {self.university.name}"

class AdmissionCriteria(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    year = models.IntegerField()
    quota = models.IntegerField()
    benchmark_score = models.FloatField()
    combination = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ['major', 'year']
    
    def __str__(self):
        return f"{self.major.code} - {self.year}"
    
    def get_blocks(self):
        return [block.strip() for block in self.combination.split(',')]