from django.contrib import admin
from employee_app.models import *

# Register your models here.
admin.site.register(DepartmentModel)
admin.site.register(EmployeeModel)
admin.site.register(SalaryModel)