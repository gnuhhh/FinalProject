from django.shortcuts import render
from school.models import School, SchoolMajor
# Create your views here.
def university(request):
    universites = School.objects.filter(type='Đại học')
    return render(request, 'university.html', {'universities':universites})

def universityHaNoi(request):
    universities = School.objects.filter(type='Đại học', location='Hà Nội')
    return render(request, 'university.html', {'universities':universities})

def universityTphcm(request):
    universities = School.objects.filter(type='Đại học', location='TP.HCM')
    return render(request, 'university.html', {'universities':universities})

def unidetail(request, k):
    uni = School.objects.get(id=k)
    school_majors = SchoolMajor.objects.filter(school=uni).select_related('major')
    return render(request, 'university_detail.html', {'uni':uni, 'school_majors':school_majors})