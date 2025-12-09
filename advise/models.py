from django.db import models
from homepage.models import Expert
from user_profile.models import Member
from datetime import timedelta, datetime, date, time
from chat.models import ChatGroup
from django.utils import timezone
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
    
    def check_date(self):
        today = date.today()
        if self.date < today:
            return True
        if self.date == today:
            now = datetime.now().time()
            if self.work_shift.start_time <= now :
                return True
        return False
    
    def __str__(self):
        return str(self.expert) + ' - ' + str(self.work_shift) + ' - ' + str(self.date)

class Room(models.Model):
    zoom_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
class Appointment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)
    zoom_room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    chat_group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, null=False, related_name='appointment')
    status = models.CharField(
        max_length=20,
        choices=[('Y', 'Đã xong'), ('P', 'Đang thực hiện'), ('N', 'Chưa thực hiện'), ('C', 'Đã hủy')],
        default='N'
    )

    def __str__(self):
        return str(self.id) + str(self.member) + ' - ' + str(self.work_schedule) + str(self.chat_group) 

    @property
    def is_greater_than_3hours(self):
        now = timezone.localtime()
        start_date = datetime.combine(self.work_schedule.date, self.work_schedule.work_shift.start_time)
        start_date = timezone.make_aware(start_date)
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

