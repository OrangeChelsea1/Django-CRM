from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

def home(request):
    # 检查是否正在登录
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 验证用户
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In！")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again..")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')  # 这里是登出后重定向的地方


def register_user(request):
    return render(request, 'register.html', {})