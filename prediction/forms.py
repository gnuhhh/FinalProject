# prediction/forms.py
from django import forms
from .models import University, MajorGroup, Major, AdmissionCriteria

# Giữ lại các form để sử dụng sau này nếu cần
class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'code', 'region']

class MajorGroupForm(forms.ModelForm):
    class Meta:
        model = MajorGroup
        fields = ['name', 'code']

class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ['name', 'code', 'university', 'major_group']

class AdmissionCriteriaForm(forms.ModelForm):
    class Meta:
        model = AdmissionCriteria
        fields = ['major', 'year', 'quota', 'benchmark_score', 'combination']