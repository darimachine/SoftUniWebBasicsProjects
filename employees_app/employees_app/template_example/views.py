from django.shortcuts import render

# Create your views here.
from employees.models import Employee,Department




def index(request):
    context={
        'title':'Employees list',
        'numbers':[123,200,342],
        'employees':Employee.objects.order_by('first_name','last_name'),
        'department_names':[d.name for d in Department.objects.all()],
    }
    return render(request,'template_example.html',context)