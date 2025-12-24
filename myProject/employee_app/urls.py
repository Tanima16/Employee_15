

from django.urls import path
from employee_app.views import *

urlpatterns = [
    
    path('',homePage,name='home'),
    path('department',departmentPage,name='department'),
    path('employee',employeePage,name='employee'),
    
    path('editdepartment/<int:id>',editdepartmentPage,name='editdepartment'),
    path('deletedepartment/<int:id>',deletedepartmentPage,name='deletedepartment'),
    
    path('editemployee/<int:id>',editdepartmentPage,name='editemployee'),
    path('deleteemployee/<int:id>',deletedepartmentPage,name='deleteemployee'),
    
]
