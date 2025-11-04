from django.db import models
from homepage.models import Expert
from user_profile.models import Member
from chat.models import ChatGroup
from datetime import timedelta, datetime
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

class Room(models.Model):
    zoom_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
class Appointment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)
    zoom_room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Y', 'Đã xong'), ('P', 'Đang thực hiện'), ('N', 'Chưa thực hiện')],
        default='N'
    )

    @property
    def is_greater_than_3hours(self):
        now = timezone.localtime()
        start_date = datetime.combine(self.work_schedule.date, self.work_schedule.work_shift.start_time)
        start_date = datetime.make_aware(start_date)
        diff = start_date - now
        return diff >= timedelta(hours=3)

class Invoice(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='invoices')
    invoice_id = models.CharField(max_length=15, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=3, default=200.000)
    status = models.CharField(
        max_length=20,
        choices=[('N', 'Chưa thanh toán'), ('Y', 'Đã thanh toán')],
        default='N'
    )

