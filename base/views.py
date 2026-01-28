from django.shortcuts import render,redirect
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
    
def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        gender=request.POST['gender']
        subject=request.POST['subject']
        mock=request.POST['mock']
        Student.objects.create(name=name,age=age,gender=gender,email=email,subject=subject,mock=mock)
        return redirect('home')
    else:   
        return render(request,'create.html')
