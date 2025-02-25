from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . forms import LoginForm
from . models import Attendance,Student
# Create your views here.

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect(reverse("attendance_records:index"))
            
    return render(request,"attendance_records/login.html",{'title':'Login','form':form,'style':'forms'})



def index_view(request):
    students = Student.objects.all()
    return render(request,'attendance_records/index.html',{'students':students})
   
def logout_view(request):
    logout(request)
    return redirect(reverse("index"))