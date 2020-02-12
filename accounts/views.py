from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'username has already been taken'})
            except User.doesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'password must match'})
    else:
        return render(request,'accounts/signup.html')
def login(request):
    return render(request,'accounts/signup.html')
def logout(request):
    return render(request,'signup.html')
