from django.shortcuts import render
from school.models import School, SchoolMajor
# Create your views here.
def college(request):
    colleges = School.objects.filter(type='Cao đẳng')
    return render(request, 'college.html', {'colleges':colleges})

def collegeHaNoi(request):
    colleges = School.objects.filter(type='Cao đẳng', location='Hà Nội')
    return render(request, 'college.html', {'colleges':colleges})

def collegeTphcm(request):
    colleges = School.objects.filter(type='Cao đẳng', location='TP.HCM')
    return render(request, 'college.html', {'colleges':colleges})

def collegedetail(request, k):
    colleges = School.objects.get(id=k)
    school_majors = SchoolMajor.objects.filter(school=colleges).select_related('major')
    return render(request, 'college_detail.html', {'colls':colleges, 'school_majors':school_majors})