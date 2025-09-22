from django.shortcuts import render, redirect
from django.contrib import auth, messages
from school.models import School
from news.models import News
from homepage.models import Expert
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from advise.models import WorkShift, WorkSchedule
from datetime import datetime, date

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
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        try:
            expert = Expert.objects.get(id = request.user.id)
            work_shift = WorkShift.objects.get(start_time = start_time, end_time=end_time)
            schedule_date = datetime.strptime(date, '%Y-%m-%d').date()
            work_schedule = WorkSchedule.objects.create(expert=expert, work_shift=work_shift, date=schedule_date, is_booked=True
            )
            messages.success(request, 'Đăng ký lịch tư vấn thành công!')
            return redirect('schedule')
            
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
            return redirect('schedule')
    else:
        work_shifts = WorkShift.objects.all().order_by('start_time')
        return render(request, 'admin/schedule/view.html', {'work_shifts': work_shifts})