from django.shortcuts import render
from .models import School, SchoolMajor
# Create your views here.
def school(request):
    schools = School.objects.all()
    return render(request, 'school.html', {'schools':schools})

def school_hanoi(request):
    schools = School.objects.filter(location="Hà Nội")
    return render(request, 'school.html', {'schools':schools})

def school_tphcm(request):
    schools = School.objects.filter(location="TP.HCM")
    return render(request, 'school.html', {'schools':schools})

def school_by_id(request, id):
    school = School.objects.get(id=id)
    school_majors = SchoolMajor.objects.filter(school=school).select_related('major')
    return render(request, 'school_detail.html', {'school':school, 'school_majors':school_majors})