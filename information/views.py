from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def bodybuilding(request):
    if request.user.is_authenticated:
        return render(request,'bb.html')
    else:
        return render(request,'login.html')

def cardio(request):
    if request.user.is_authenticated:
        return render(request,'cardio.html')
    else:
        return render(request,'login.html')
