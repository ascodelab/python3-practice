from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request): 
    return render(request,'saurabh/index.html')

def about(request): 
    return render(request,'saurabh/about.html')

def contact(request): 
    return render(request,'saurabh/contact.html')