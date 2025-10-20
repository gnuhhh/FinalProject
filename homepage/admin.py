from django.contrib import admin
from .models import Expert, ChatHistory
# Register your models here.
admin.site.register([Expert, ChatHistory])