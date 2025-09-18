from django.contrib import admin
from .models import WorkSchedule, WorkShift
# Register your models here.
admin.site.register([WorkSchedule, WorkShift])