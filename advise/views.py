from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from homepage.models import Expert
# Create your views here.

@login_required(login_url='login')
def index(request):
    expert = Expert.objects.all()
    return render(request, 'advise.html', {'expert':expert})