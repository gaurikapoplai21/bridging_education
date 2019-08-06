from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse('<h1> About Us </h1>')

def FAQ (request):
    return HttpResponse('<h1> FAQ </h1>')

def ContactUs (request):
    return HttpResponse('<h1> Contact Us </h1>')


                        
