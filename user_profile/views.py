from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         request.user.email = request.POST['email'].strip()
#         request.user.first_name = request.POST['firstname'].strip()
#         request.user.last_name = request.POST['lastname'].strip()
#         request.user.save()
#         messages.success(request, 'Cập nhật thành công')
#         return redirect('user_profile')
#     else:
#         return render(request, 'user_profile.html')
    
def index(request):
    return render(request, 'user_profile.html')


        