from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages  
# contact m confirm recieve message k leye

# Create your views here.


def index(request):
    context = {
        'variable1': "Here Computer Acessories  available ", 
        'variable2': "Here Printer Service available "
    }
    # messages.success(request, "This is a Test massage")
    return render(request, 'index.html', context)

    # return HttpResponse('This is Super Computer Home Page')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is About Page')

def services(request):
    return render(request, 'services.html')

def computer(request):
    return render(request, 'computer.html')

def laptop(request):
    return render(request, 'laptop.html')

def mobile(request):
    return render(request, 'mobile.html')

def speaker(request):
    return render(request, 'speaker.html')

def printer(request):
    return render(request, 'printer.html')

def others(request):
    return render(request, 'others.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.') 
        # contact send message confirm k leye
        # net pr django messages servicess me pata chale ga 
    return render(request, 'contact.html')
    
