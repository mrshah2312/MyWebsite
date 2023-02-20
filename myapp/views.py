from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randint
from django.contrib import messages
import random

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def signup_page(request):
    return render(request, 'signup.html')

def signin_page(request):
    return render(request, 'signin.html')

def cotp_page(request):
    return render(request, 'cotp.html')

def aotp_page(request):
    return render(request, 'aotp.html')

def Signup(request):
    if request.POST['password'] == request.POST['cpassword']:
        try:
            Master.objects.get(Email=request.POST['email'])
            message = "Email Already Exits"
        except Master.DoesNotExist:
            master = Master.objects.create(Email=request.POST['email'],Password=request.POST['password'])
            otp=random.randint(1000,9999)
            subject = 'This Is Your Account Conformation Mail'
            message = "Hello there, Your OTP : "+str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [master.Email,]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'cotp.html',{'email':master.Email,'otp':otp})
    else:      
        return render(request,'signup.html')

def cotp(request):
    email=request.POST['email']
    otp=request.POST['otp']
    uotp=request.POST['uotp']
    if otp==uotp:
        return render(request,'signin.html',{'email':email})

    else:
        msg="Invalid OTP"
        return render(request,'cotp.html',{'email':email,'msg':msg,'otp':otp})

def Signin(request):
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            otp=random.randint(1000,9999)
            subject = 'This Is Your Account Activation Mail '
            message = "Hello there, Your OTP : "+str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [master.Email,]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, "Welcome to GrossyFy.")
            return render(request, 'aotp.html',{'email':master.Email,'otp':otp})
        else:
            messages.success(request, "Password Does Not Match.")
            return render(request,"signin.html")
        
    except Master.DoesNotExist:
        messages.error(request, "User Does Not Exist.")
        return render(request,"signin.html")

def aotp(request):
    email=request.POST['email']
    otp=request.POST['otp']
    uotp=request.POST['uotp']
    if otp==uotp:
        return render(request,'index.html',{'email':email})

    else:
        msg="Invalid OTP"
        return render(request,'aotp.html',{'email':email,'msg':msg,'otp':otp})