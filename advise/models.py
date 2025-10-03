from django.db import models
from homepage.models import Expert
from user_profile.models import Member
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

class Appointment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('Y', 'Đã xong'), ('P', 'Đang thực hiện'), ('N', 'Chưa thực hiện')]
    )
