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
class EmployeeForm(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )
    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError('This is a bot')

    class Meta:
        model=Employee
        fields='__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control'}
            )
        }
class EditEmployeeForm(EmployeeForm):



    class Meta:
        model = Employee
        fields = '__all__'
        widgets={
            'egn':forms.TextInput(
                attrs={"readonly":"readonly"}
            )
        }
# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Enter first name',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'form-control',
#             }
#         )
#     )
#     last_name = forms.CharField(
#         max_length=40,
#     )
#     egn = forms.CharField(
#         max_length=10,
#     )
#     job_title = forms.ChoiceField(
#            choices=(
#             (1, 'Software Developer'),
#             (2, 'QA Engineer'),
#             (3, 'DevOps Specialist')
#            )
#     )
#     company = forms.ChoiceField(
#         choices=((c, c) for c in Employee.COMPANIES)
#     )

class EmployeeOrderForm(forms.Form):
    order_by =forms.ChoiceField(
        choices=(
            ('first_name','First name'),
            ('last_name','Last name'),
        ),
        # required=False,
    )
def home(request):
    print(request.user)

    return render(request,'index.html')

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
       employee_form = EmployeeForm(request.POST,request.FILES)
       if employee_form.is_valid():
           # emp = Employee(
           #     first_name=employee_form.cleaned_data['first_name'],
           #     last_name =employee_form.cleaned_data['last_name'],
           #     egn= employee_form.cleaned_data['egn'],
           #     job_title=employee_form.cleaned_data['job_title'],
           #     company=employee_form.cleaned_data['company'],
           #     deparment_id=1,
           #
           # )

           employee_form.save()
           return redirect('details')
    else:
        employee_form=EmployeeForm()
    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by','first_name')
    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form
    }
    return render(request, 'create.html', context)

def edit_employee(request,pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee_form = EditEmployeeForm(request.POST,request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create_employee')
    else:
        employee_form = EditEmployeeForm(instance=employee)
    context = {
        'employee': employee,
        'employee_form': employee_form,
    }
    return render(request, 'edit.html', context)