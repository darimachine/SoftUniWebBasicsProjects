import random

from django.core.exceptions import ValidationError
from django.forms import NumberInput
from django.http import HttpResponse
from django.shortcuts import render, redirect
from htmlmin.decorators import minified_response
from django import forms
# Create your views here.
from employees.models import Department

from employees.models import Employee

def validate_positive(value):
    if value <0:
        raise ValidationError('Value must be positive')

class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        label='Enter first name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    last_name = forms.CharField(
        max_length=40,
    )
    age = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',

            }
        ),
        validators=[validate_positive]
    )


def home(request):
    print(request.user)

    return render(request,'index.html',context)

def department_details(request):
    print(Department.objects.get(name='Tv App'))
    print(Department.objects.filter(name='Tv App'))
    context={
        'departments':Department.objects.all(),
        'employees': Employee.objects.all(),
        'employee_form':EmployeeForm(),
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

def create_employee(request):
    if request.method=='POST':
       employee_form = EmployeeForm(request.POST)
       if employee_form.is_valid():
           return redirect('details')
    else:
        employee_form=EmployeeForm()

    context = {
        'employee_form': employee_form,
    }
    return render(request, 'create.html', context)
