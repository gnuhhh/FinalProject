from django.shortcuts import render, redirect
from user_profile.models import Member
from advise.models import Appointment, Invoice  
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def show_info(request):
    member = get_object_or_404(Member, id=request.user.id)
    if request.method == 'POST':
        if 'avatar' in request.FILES:
            member.avatar = request.FILES['avatar']
        member.first_name = request.POST['first_name']
        member.last_name = request.POST['last_name']
        member.email = request.POST['email']
        member.phone_number = request.POST['phone']
        member.gender = request.POST['gender']
        if request.POST['dob']:
            member.birthdate = request.POST['dob']
        member.save()
        messages.success(request, "Thay đổi thành công")
        return redirect('user_profile')
    else:
        appointments = Appointment.objects.filter(member=member, invoices__status='Y').order_by('-work_schedule__date', '-work_schedule__work_shift__start_time')
        invoices = Invoice.objects.all().order_by('-invoice_id')
        return render(request, 'userprofile.html', {'member':member, 'appointments':appointments, 'invoices':invoices})
    
def cancel_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.status = 'C'
    appointment.save()
    messages.success(request, "Hủy lịch hẹn thành công")
    return redirect('user_profile')
        


        