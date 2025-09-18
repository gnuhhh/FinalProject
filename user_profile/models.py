from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Member(User):
    avatar = models.ImageField(upload_to='static/assets/img/members/', blank=True)
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
        db_table = 'Members'