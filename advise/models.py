from django.db import models
from homepage.models import Expert
# Create your models here.
class WorkSchedule(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='schedule')
    date = models.DateField()
    is_booked = models.BooleanField(default=False)

class WorkShift(models.Model):
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE, related_name='shift')
    start_time = models.TimeField()
    end_time = models.TimeField()