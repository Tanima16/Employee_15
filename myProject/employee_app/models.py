from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    name=models.CharField(max_length=30,null=True)
    description=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class EmployeeModel(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    phone=models.IntegerField(null=True)
    department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name

class SalaryModel(models.Model):
    employee=models.OneToOneField(EmployeeModel,on_delete=models.SET_NULL,null=True)
    basic_salary=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    bonus_per=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    total_salary=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    
    def __str__(self):
        return self.salary