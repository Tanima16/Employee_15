from django.shortcuts import render,redirect
from employee_app.models import *

# Create your views here.
def homePage(request):
    
    return render(request,'home.html')

def departmentPage(request):
    department=DepartmentModel.objects.all()  
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        
        DepartmentModel.objects.create(
            name=name,
            description=description,
        )
        
    return render(request,'department.html',{'department':department})

def deletedepartmentPage(request,id):
   department= DepartmentModel.objects.get(id=id).delete()
   return redirect('department')

def editdepartmentPage(request,id):
    dt=DepartmentModel.objects.get(id=id)
    if request.method=="POST":
       name=request.POST.get('name')
       description=request.POST.get('description')
       
       dt.name=name
       dt.description=description
       dt.save()
       return redirect('department')  
    context={
        'dt':dt
    }
         
         
    return render(request,'editdepartment.html',context)



#...............EMPLOYEE.........

def employeePage(request):
    department=DepartmentModel.objects.all()
    employee=EmployeeModel.objects.all()
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        department_id=request.POST.get('department')
        
        dt=DepartmentModel.objects.get(id=department_id)
        EmployeeModel(
            name=name,
            email=email,
            phone=phone,
            department=dt,
            
        ).save()
        return redirect('employee')
        
    return render(request,'employee.html',{'employee':employee,'department':department})