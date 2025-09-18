from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Expert(User):
    avatar = models.ImageField(upload_to='static/assets/img/experts', blank=True)
    description = models.CharField(max_length=200, verbose_name='Mô tả', null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10
        , blank=True
        , choices=[('Male', 'Nam'), ('Female', 'Nữ'), ('Other', 'Khác')] 
        )
    phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    class Meta:
        db_table = "Experts"