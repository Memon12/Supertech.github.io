from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("Home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("computer", views.computer, name='computer'),
    path("mobile", views.mobile, name='mobile'),
    path("laptop", views.laptop, name='laptop'),
    path("printer", views.printer, name='printer'),
    path("speaker", views.speaker, name='speaker'),
    path("others", views.others, name='others'),

]

