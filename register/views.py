from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password != password2:
            messages.error(request, 'Mật khẩu xác nhận không khớp!')
            return redirect('register')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Tên đăng nhập đã được sử dụng!')
            return redirect('register')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email đã được sử dụng!')
            return redirect('register')
            
        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name = firstname, last_name = lastname)
            user.save()
            messages.success(request, 'Đăng ký thành công!')
            return redirect('login')  
            
        except Exception as e:
            messages.error(request, f'Lỗi: {str(e)}')
            return redirect('register')
    else:   
        return render(request, 'register.html')