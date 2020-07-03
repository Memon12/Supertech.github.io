from django.shortcuts import render, HttpResponse

# pasward user:admin, pasward:Super12!
# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse ("This is  Home page")


def about(request):
    return HttpResponse ("This is  about page")

def services(request):
    return HttpResponse ("This is  services page")

def contact(request):
    return render(request, 'contact.html')

