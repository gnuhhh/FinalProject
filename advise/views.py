from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.utils import timezone
from django.conf import settings
from advise.vnpay import vnpay
import hashlib
import urllib.parse
from homepage.models import Expert
from advise.models import WorkSchedule
from datetime import date, timedelta
# Create your views here.

@login_required(login_url='login')
def index(request):
    expert = Expert.objects.all()
    
    # Tạo dữ liệu lịch tuần hiện tại (từ thứ 2 đến chủ nhật)
    today = timezone.now().date()
    # Tìm thứ 2 của tuần hiện tại
    days_since_monday = today.weekday()  # 0 = Monday, 6 = Sunday
    monday = today - timedelta(days=days_since_monday)
    
    week_dates = []
    for i in range(7):  # 7 ngày từ thứ 2 đến chủ nhật
        current_date = monday + timedelta(days=i)
        # Lấy tất cả lịch của tất cả chuyên gia cho ngày này
        schedules = WorkSchedule.objects.filter(
            date=current_date
        ).select_related('expert', 'work_shift').order_by('work_shift__start_time')
        
        week_dates.append({
            'date': current_date,
            'schedules': schedules
        })
    
    return render(request, 'advise.html', {
        'expert': expert,
        'week_dates': week_dates
    })


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

@login_required(login_url='login')
def expert_schedule(request):
    """API endpoint để lấy lịch của chuyên gia"""
    expert_id = request.GET.get('expert_id')
    if not expert_id:
        return HttpResponseBadRequest('Missing expert_id')
    
    try:
        expert = Expert.objects.get(id=expert_id)
    except Expert.DoesNotExist:
        return HttpResponseBadRequest('Invalid expert_id')
    
    # Tạo dữ liệu lịch tuần hiện tại (từ thứ 2 đến chủ nhật)
    today = timezone.now().date()
    # Tìm thứ 2 của tuần hiện tại
    days_since_monday = today.weekday()  # 0 = Monday, 6 = Sunday
    monday = today - timedelta(days=days_since_monday)
    
    schedule_data = []
    for i in range(7):  # 7 ngày từ thứ 2 đến chủ nhật
        current_date = monday + timedelta(days=i)
        # Lấy lịch của chuyên gia cho ngày này
        schedules = WorkSchedule.objects.filter(
            expert=expert,
            date=current_date
        ).select_related('work_shift').order_by('work_shift__start_time')
        
        schedule_list = []
        for schedule in schedules:
            schedule_list.append({
                'id': schedule.id,
                'start_time': schedule.work_shift.start_time.strftime('%H:%M'),
                'end_time': schedule.work_shift.end_time.strftime('%H:%M'),
                'is_booked': schedule.is_booked
            })
        
        schedule_data.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'schedules': schedule_list
        })
    
    return JsonResponse({'schedule': schedule_data})


def payment(request):
    if request.method == 'POST':
        # Process input data and build url payment
        form = PaymentForm(request.POST)
        if form.is_valid():
            order_type = form.cleaned_data['order_type']
            order_id = form.cleaned_data['order_id']
            amount = form.cleaned_data['amount']
            order_desc = form.cleaned_data['order_desc']
            bank_code = form.cleaned_data['bank_code']
            language = form.cleaned_data['language']
            ipaddr = get_client_ip(request)
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.1.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = amount * 100
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = order_id
            vnp.requestData['vnp_OrderInfo'] = order_desc
            vnp.requestData['vnp_OrderType'] = order_type
            # Check language, default: vn
            if language and language != '':
                vnp.requestData['vnp_Locale'] = language
            else:
                vnp.requestData['vnp_Locale'] = 'vn'
                # Check bank_code, if bank_code is empty, customer will be selected bank on VNPAY
            if bank_code and bank_code != "":
                vnp.requestData['vnp_BankCode'] = bank_code

            vnp.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')  # 20150410063022
            vnp.requestData['vnp_IpAddr'] = ipaddr
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
            vnpay_payment_url = vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)
            print(vnpay_payment_url)
            return redirect(vnpay_payment_url)
        else:
            print("Form input not validate")
    else:
        return render(request, "payment.html", {"title": "Thanh toán"})