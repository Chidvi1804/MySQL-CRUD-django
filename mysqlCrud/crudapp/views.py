from django.shortcuts import render,redirect
from .models import Employee
from .forms import Employeeform

def addnew(request):
    if request.method=='POST':
        form=Employeeform(request.POST)
        if form.is_valid():
            try:
                 form.save()
                 return redirect('/')
            except:
                pass
    else:
        form=Employeeform() 
    return render(request,'index.html',{'form':form})

def index(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees})

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})
    

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=Employeeform(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request,'edit.html',{'employee':employee})

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")




