from django.db import models
from homepage.models import Expert
# Create your models here.
class WorkShift(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time) + ' - ' + str(self.end_time)
class WorkSchedule(models.Model):
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='schedule')
    work_shift = models.ForeignKey(WorkShift, on_delete=models.CASCADE, related_name='shift')
    date = models.DateField()
    is_booked = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=[('Y', 'Đã được duyệt'), ('P', 'Đang chờ duyệt'), ('C', 'Đã hủy')],
        default='P'
    )

