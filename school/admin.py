from django.contrib import admin
from .models import School, Major, SchoolMajor
# Register your models here.
admin.site.register(School)
admin.site.register(Major)
admin.site.register(SchoolMajor)