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
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age', '').strip()
        email = request.POST.get('email', '').strip()
        gender = request.POST.get('gender', '').strip()
        subject = request.POST.get('subject', '').strip()
        mock = request.POST.get('mock', '').strip()

        if not all([name, age, email, gender, subject, mock]):
            error = "All fields are mandatory"
            context = {
                'error': error,
                'name': name,
                'age': age,
                'email': email,
                'gender': gender,
                'subject': subject,
                'mock': mock,
            }
            return render(request, 'create.html', context)
        else:
            Student.objects.create(
                name=name,
                age=age,
                gender=gender,
                email=email,
                subject=subject,
                mock=mock
            )
            return redirect('home')


    return render(request, 'create.html')

    
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
