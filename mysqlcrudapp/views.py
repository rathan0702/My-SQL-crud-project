from django.shortcuts import render,redirect
from mysqlcrudapp.models import Employee
from mysqlcrudapp.forms import EmployeeForm
from django.contrib import messages

# Create your views here.
def insert(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'record inserted succuessfully')
        else:
            messages.info(request,"please enter the correct details")
    else:
        form = EmployeeForm()
    return render(request,"index.html",{'form':form})

def show(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees})

def delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/show')

def edit(request,id):
    emp=Employee.objects.get(id=id)
    return render(request,'edit.html',{'emp':emp})

def update(request,id):
    emp=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=emp)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'emp':emp})



