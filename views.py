
from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages,auth
from django.db import models
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def myindex(request):
    return render(request,'index.html')

def myabout(request):
    return render(request,'about-us.html')
    
def mycontact(request):
    
    if request.method == "POST":
        
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        comment=request.POST['comment']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(comment)<4:
            messages.error(request,"Please fill the form correctly")
        else:
            contact=Contact(name=name,email=email,phone=phone,comment=comment)
            contact.save()
            messages.success(request, 'Thanks For Contacting Us')

        #send an email
        send_mail(
            'Message From Website',
            comment,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
        
       
    return render(request,'contact.html')


def myfeatures(request):
    return render(request,'features.html')

def myprojects(request):
    return render(request,'projects.html')


