from django.contrib import admin
from .models import WorkSchedule, WorkShift, Appointment, Invoice
# Register your models here.
admin.site.register([WorkSchedule, WorkShift, Appointment, Invoice])