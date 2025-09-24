from django.shortcuts import render, redirect
from django.contrib import auth, messages
from school.models import School
from news.models import News
from homepage.models import Expert
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from advise.models import WorkShift, WorkSchedule
from datetime import datetime, date
import calendar

# Create your views here.
def loginadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff == True:
                auth.login(request, user)
                messages.success(request, 'Đăng nhập thành công!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Bạn không có quyền truy cập')
                return redirect('admin')
        else:
            messages.info(request, 'Thông tin đăng nhập không tồn tại')
            return redirect('admin')
    else:
        return render(request, 'loginadmin.html')
    
def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff == True:
            return render(request, 'dashboard.html', {'user':request.user})
        else:
            return render(request, 'loginadmin.html')
    else:
        return render(request, 'loginadmin.html')
    
def information(request):
    schools = School.objects.all()
    return render(request, 'admin/information/view.html', {'schools':schools})

def information_create(request):
    if request.method == 'POST':
        schoolId = request.POST['schoolId']
        schoolName = request.POST['schoolName']
        type = request.POST['type']
        location = request.POST['location']
        content = request.POST['content']
        
        school = School(
            schoolId=schoolId,
            schoolName=schoolName,
            type=type,
            location=location,
            content=content
        )
        school.save()
        
        messages.success(request, 'Thêm trường thành công!')
        return redirect('information')
    else:
        return render(request, 'admin/information/update_create.html', {'title': 'Thêm trường mới'})

def information_update(request, id):
    school = School.objects.get(id=id)
    
    if request.method == 'POST':
        school.schoolId = request.POST['schoolId']
        school.schoolName = request.POST['schoolName']
        school.type = request.POST['type']
        school.location = request.POST['location']
        school.content = request.POST['content']
        school.save()
        messages.success(request, 'Cập nhật thông tin trường thành công!')
        return redirect('information')
    else:
        return render(request, 'admin/information/update_create.html', {
            'school': school,
            'title': 'Cập nhật thông tin trường'
        })

def information_delete(request, id):
    school = School.objects.get(id=id)
    school.delete()
    messages.success(request, 'Xóa trường thành công!')
    return redirect('information')

def news(request):
    news_list = News.objects.all().order_by('id')
    return render(request, 'admin/news/view.html', {'news_list':news_list})

def news_create(request):
    if request.method == 'POST':
        title = strip_tags(request.POST['title'])
        content = strip_tags(request.POST['content'])
        author = strip_tags(request.POST['author'])
        news = News(title=title, content=content, author=author)
        news.save()
        messages.success(request, 'Thêm thành công!')
        return redirect('news')
    else:
        return render(request, 'admin/news/update_create.html', {"title":'Thêm tin tức'})
    
def news_update(request, id):
    new = News.objects.get(id=id)
    if request.method == 'POST':
        new.title = request.POST['title']
        new.content = strip_tags(request.POST['content'])
        new.author = request.POST['author']
        new.save()
        messages.success(request, 'Cập nhật bài viết thành công')
        return redirect('news')
    else:
        return render(request, 'admin/news/update_create.html', {'new':new, 'title':'Cập nhật tin tức'})
    
def news_delete(request, id):
    new = News.objects.get(id=id)
    new.delete()
    messages.success(request, 'Xóa thành công')
    return redirect('news')

def accounts(request):
    users = User.objects.all()
    return render(request, 'admin/account/view.html', {'users':users})

def accounts_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, 'Xóa thành công')
    return redirect('accounts')

def accounts_create(request):
    return render(request, 'admin/account/update_create.html')

def schedule(request):
    if request.method == 'POST':
        selected_date_str = request.POST.get('date')
        shift_id = request.POST.get('shift_id')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        try:
            expert = Expert.objects.get(id=request.user.id)
            if shift_id:
                work_shift = WorkShift.objects.get(id=shift_id)
            else:
                work_shift = WorkShift.objects.get(start_time=start_time, end_time=end_time)
            schedule_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
            WorkSchedule.objects.create(
                expert=expert,
                work_shift=work_shift,
                date=schedule_date,
                is_booked=True,
            )
            messages.success(request, 'Đăng ký lịch tư vấn thành công!')
            return redirect('schedule')
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
            return redirect('schedule')
    else:
        # Determine current view month/year
        today = date.today()
        try:
            year = int(request.GET.get('year', today.year))
            month = int(request.GET.get('month', today.month))
        except ValueError:
            year, month = today.year, today.month

        # Selected date (within the shown month ideally)
        selected_date_str = request.GET.get('selected_date')
        try:
            selected_date = (
                datetime.strptime(selected_date_str, '%Y-%m-%d').date()
                if selected_date_str
                else today
            )
        except Exception:
            selected_date = today

        # Build calendar matrix (weeks -> days)
        cal = calendar.Calendar(firstweekday=0)  # Monday=0? In Python, Monday=0; Sunday=6
        month_days = list(cal.itermonthdates(year, month))
        # Group into weeks of 7 days
        weeks = []
        for i in range(0, len(month_days), 7):
            weeks.append(month_days[i:i + 7])

        # Shifts and booked info for selected date
        work_shifts = list(WorkShift.objects.all().order_by('start_time'))
        booked_shift_ids = set(
            WorkSchedule.objects.filter(date=selected_date, is_booked=True)
            .values_list('work_shift_id', flat=True)
        )

        # Navigation months
        prev_month_date = date(year, month, 1) - date.resolution
        prev_month_year = (prev_month_date.replace(day=1)).year
        prev_month = (prev_month_date.replace(day=1)).month
        next_month_base = date(year, month, calendar.monthrange(year, month)[1]) + date.resolution
        next_month_year = (next_month_base.replace(day=1)).year
        next_month = (next_month_base.replace(day=1)).month

        context = {
            'year': year,
            'month': month,
            'weeks': weeks,
            'selected_date': selected_date,
            'work_shifts': work_shifts,
            'booked_shift_ids': booked_shift_ids,
            'month_label': f"Tháng {month} {year}",
            'prev_year': prev_month_year,
            'prev_month': prev_month,
            'next_year': next_month_year,
            'next_month': next_month,
        }
        return render(request, 'admin/schedule/view.html', context)

def expert_view(request):
    expert = Expert.objects.all()
    return render(request, 'admin/expert/view.html', {'expert':expert})

def expert_delete(request, id):
    expert = Expert.objects.get(id=id)
    expert.delete()
    messages.success(request, 'Xóa thành công')
    return redirect('expert')

def expert_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        avatar = request.FILES.get('avatar')
        email = request.POST.get('email')
        description = request.POST['description']
        username = request.POST['username']
        password = request.POST['password']
        expert = Expert(first_name=first_name, last_name=last_name, avatar=avatar, email=email, description=description, username=username)
        expert.set_password(password)
        expert.is_staff = True
        expert.save()
        messages.success(request, 'Thêm thành công')
        return redirect('expert')
    else:    
        return render(request, 'admin/expert/create.html', {'title':'Thêm chuyên gia'})
    
def expert_update(request, id):
    expert = Expert.objects.get(id=id)
    if request.method == 'POST':
        expert.first_name = request.POST['first_name']
        expert.last_name = request.POST['last_name']
        if 'avatar' in request.FILES:
            expert.avatar = request.FILES['avatar']
        expert.email = request.POST['email']
        expert.description = request.POST['description']
        expert.save()
        messages.success(request, 'Cập nhật thành công')
        return redirect('expert')
    else:
        return render(request, 'admin/expert/update.html', {'expert':expert, 'title':'Cập nhật chuyên gia'})