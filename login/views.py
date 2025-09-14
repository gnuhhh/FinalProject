from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'Đăng nhập thành công!')
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Thông tin đăng nhập không tồn tại')
            return redirect('login')
    else:
        return render(request, 'login.html')