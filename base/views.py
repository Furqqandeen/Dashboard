from django.shortcuts import render,redirect
from django.http import HttpResponse
from base.models import Student
from django.db.models import Q
from django.shortcuts import get_object_or_404

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
    
def delete(request,pk):
    std=get_object_or_404(Student,pk=pk)
    std.delete()
    return redirect('home')

def update(request,pk):
    std=Student.objects.get(id=pk)
    if request.method=='POST':
        
        std.name=request.POST['name']
        std.age=request.POST['age']
        std.email=request.POST['email']
        std.gender=request.POST['gender']
        std.subject=request.POST['subject']
        std.mock=request.POST['mock']
        std.save()
        return redirect('home')
    else:
        return render(request,'update.html',{'student':std})
