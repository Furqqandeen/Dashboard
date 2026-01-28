from django.shortcuts import render
from django.http import HttpResponse
from base.models import Student

# Create your views here.

def home(request):
    details={
        'Students':Student.objects.all()
    }
    return render(request,'home.html',details)
