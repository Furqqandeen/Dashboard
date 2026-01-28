from django.shortcuts import render
from django.http import HttpResponse
from base.models import Student
from django.db.models import Q

# Create your views here.

def home(request):
    details={
        'Students':Student.objects.all()
    }
    return render(request,'home.html',details)

def search(request):
    if request.method=="GET":
        keyword=request.GET['word']
        details={
            'Students':Student.objects.all().filter(Q(name__icontains=keyword)|Q(subject__icontains=keyword))
        }
        return render(request,'home.html',details)
