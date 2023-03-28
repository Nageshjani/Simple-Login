from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginView(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is None:
            messages.error(request,'Invalid Credentials')
        else:
            login(request,user)
            return redirect('home')
    else:
        return render(request,'myapp/login.html')
            





@login_required
def home(request):
    return render(request,'myapp/home.html')