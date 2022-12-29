from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
# Create your views here.
def home(request):
    items = Task.objects.all()
    items_string = [f"{t.title}"for t in items]


    return render(request,'home.html',context={'items':items_string})