import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from htmlmin.decorators import minified_response

# Create your views here.
from employees.models import Department

from employees.models import Employee


def home(request):
    print(request.user)

    context={
        'number':random.randint(0,100)
    }
    return render(request,'index.html',context)

def department_details(request):
    print(Department.objects.get(name='Tv App'))
    print(Department.objects.filter(name='Tv App'))
    context={
        'departments':Department.objects.all(),
        'employees': Employee.objects.all(),
    }
    # for i in Employee.objects.all():
    #     print(i.deparment.name)
    j=0
    for department in Department.objects.all():
        for employee in department.employee_set.all():
            j+=1

            print(employee.first_name)
            print(j)
    print(j)
    return render(request,'list_departments.html',context=context)

def list_departments(request,id):
    return HttpResponse(f"This is department list {id} ")

def list_employees(request):
    return HttpResponse("This is list of employee")