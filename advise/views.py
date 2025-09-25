from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.utils import timezone
from django.conf import settings
import hashlib
import urllib.parse
from homepage.models import Expert
from advise.models import WorkSchedule
from datetime import date
# Create your views here.

@login_required(login_url='login')
def index(request):
    expert = Expert.objects.all()
    return render(request, 'advise.html', {'expert':expert})


@login_required(login_url='login')
def available_dates(request):
    expert_id = request.GET.get('expert_id')
    if not expert_id:
        return HttpResponseBadRequest('Missing expert_id')
    try:
        expert = Expert.objects.get(id=expert_id)
    except Expert.DoesNotExist:
        return HttpResponseBadRequest('Invalid expert_id')

    today = timezone.now().date()
    dates_qs = (
        WorkSchedule.objects
        .filter(expert=expert, date__gte=today)
        .order_by('date')
        .values_list('date', flat=True)
        .distinct()
    )
    data = [d.isoformat() for d in dates_qs]
    return JsonResponse({'dates': data})


@login_required(login_url='login')
def available_slots(request):
    expert_id = request.GET.get('expert_id')
    selected_date = request.GET.get('date')
    if not expert_id or not selected_date:
        return HttpResponseBadRequest('Missing expert_id or date')
    try:
        expert = Expert.objects.get(id=expert_id)
    except Expert.DoesNotExist:
        return HttpResponseBadRequest('Invalid expert_id')
    try:
        target_date = date.fromisoformat(selected_date)
    except Exception:
        return HttpResponseBadRequest('Invalid date')

    schedules = (
        WorkSchedule.objects
        .select_related('work_shift')
        .filter(expert=expert, date=target_date)
        .order_by('work_shift__start_time')
    )
    slots = []
    for s in schedules:
        st = s.work_shift.start_time.strftime('%H:%M') if s.work_shift.start_time else ''
        et = s.work_shift.end_time.strftime('%H:%M') if s.work_shift.end_time else ''
        slots.append({
            'shift_id': s.work_shift.id,
            'label': f"{st} - {et}",
        })
    return JsonResponse({'slots': slots})

# def vnpay_payment(request):