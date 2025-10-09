from django.contrib import admin
from .models import University, Major

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'location', 'type', 'website']
    list_filter = ['type', 'location']
    search_fields = ['name', 'code']

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'university', 'block', 'benchmark_2024', 'admission_quota']
    list_filter = ['block', 'university', 'benchmark_2024']
    search_fields = ['name', 'university__name']
    ordering = ['-benchmark_2024']