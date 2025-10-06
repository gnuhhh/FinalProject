from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils import timezone
from django.conf import settings
from advise.vnpay import vnpay
import hashlib
import hmac
import urllib.parse
import string
import random
from homepage.models import Expert
from user_profile.models import Member
from .models import WorkSchedule, Appointment, Invoice
from decimal import Decimal
from datetime import date, timedelta, datetime
# Regex for extracting invoice id from vnp_TxnRef
import re
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
            date=current_date,
            status='Y'
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
        .filter(expert=expert, status='Y', date__gte=today)
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
            date=current_date,
            status='Y'
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

def hmacsha512(key, data):
    byteKey = key.encode('utf-8')
    byteData = data.encode('utf-8')
    return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def payment(request):
    if request.method == 'POST':
        member = Member.objects.get(id=request.user.id)
        schedule_id = request.POST.get('schedule_id')
        if not schedule_id:
            return HttpResponseBadRequest('Missing schedule_id')
        try:
            work_schedule = WorkSchedule.objects.get(id=schedule_id)
        except WorkSchedule.DoesNotExist:
            return HttpResponseBadRequest('Invalid schedule_id')

        # Tạo hóa đơn trước khi chuyển hướng VNPay
        invoice = Invoice.objects.create(
            member=member,
            work_schedule=work_schedule,
            price=Decimal('200000')/1000,  # 200,000 VND
            status='N'
        )
        invoice.invoice_id=f'INV000{invoice.id}'
        invoice.save()
        
        ipaddr = get_client_ip(request)
        vnp = vnpay()
        vnp.requestData['vnp_Version'] = '2.1.0'
        vnp.requestData['vnp_Command'] = 'pay'
        vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
        vnp.requestData['vnp_Amount'] = 200000 * 100
        vnp.requestData['vnp_CurrCode'] = 'VND'
        vnp.requestData['vnp_TxnRef'] = f'INV000{invoice.id}'
        vnp.requestData['vnp_OrderInfo'] = 'thanh toan hoa don'
        vnp.requestData['vnp_OrderType'] = 'billpayment'
        vnp.requestData['vnp_Locale'] = 'vn'
        vnp.requestData['vnp_BankCode'] = 'NCB'
        vnp.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')  # 20150410063022
        vnp.requestData['vnp_IpAddr'] = ipaddr
        vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
        vnpay_payment_url = vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)
        print(vnpay_payment_url)
        return redirect(vnpay_payment_url)
    else:
        return render(request, 'advise.html')

def payment_ipn(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = inputData['vnp_Amount']
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            # Check & Update Order Status in your Database
            # Your code here
            firstTimeUpdate = True
            totalamount = True
            if totalamount:
                if firstTimeUpdate:
                    if vnp_ResponseCode == '00':
                        print('Payment Success. Your code implement here')
                    else:
                        print('Payment Error. Your code implement here')

                    # Return VNPAY: Merchant update success
                    result = JsonResponse({'RspCode': '00', 'Message': 'Confirm Success'})
                else:
                    # Already Update
                    result = JsonResponse({'RspCode': '02', 'Message': 'Order Already Update'})
            else:
                # invalid amount
                result = JsonResponse({'RspCode': '04', 'Message': 'invalid amount'})
        else:
            # Invalid Signature
            result = JsonResponse({'RspCode': '97', 'Message': 'Invalid Signature'})
    else:
        result = JsonResponse({'RspCode': '99', 'Message': 'Invalid request'})

    return result

def payment_return(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = int(inputData['vnp_Amount']) / 100
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            if vnp_ResponseCode == "00":
                return render(request, "payment_return.html", {"title": "Kết quả thanh toán",
                                                               "result": "Thành công", "order_id": order_id,
                                                               "amount": amount,
                                                               "order_desc": order_desc,
                                                               "vnp_TransactionNo": vnp_TransactionNo,
                                                               "vnp_ResponseCode": vnp_ResponseCode})
            else:
                return render(request, "payment_return.html", {"title": "Kết quả thanh toán",
                                                               "result": "Lỗi", "order_id": order_id,
                                                               "amount": amount,
                                                               "order_desc": order_desc,
                                                               "vnp_TransactionNo": vnp_TransactionNo,
                                                               "vnp_ResponseCode": vnp_ResponseCode})
        else:
            return render(request, "payment_return.html",
                          {"title": "Kết quả thanh toán", "result": "Lỗi", "order_id": order_id, "amount": amount,
                           "order_desc": order_desc, "vnp_TransactionNo": vnp_TransactionNo,
                           "vnp_ResponseCode": vnp_ResponseCode, "msg": "Sai checksum"})
    else:
        return render(request, "payment_return.html", {"title": "Kết quả thanh toán", "result": ""})
