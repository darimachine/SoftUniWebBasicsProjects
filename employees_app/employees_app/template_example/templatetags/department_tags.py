from django import template

from employees.models import Department

register = template.Library()
@register.inclusion_tag(filename='department_list.html')
def department_list():
    departments = Department.objects.all()
    return {
        'departments':departments,
    }
