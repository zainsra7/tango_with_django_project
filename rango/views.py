from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! | Here is my <b><a href='rango/about'>about</a></b> page")

def about(request):
    return HttpResponse("Rango says here is the about page. Go back to <b><a href='/'>Main</a></b> page")
