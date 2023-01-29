from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateExpenseForm,EditExpenseForm,DeleteExpenseForm
from .models import Profile, Expense


# Create your views here.
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create_profile')
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(expense.price for expense in expenses)
    context={
        'expenses':expenses,
        'profile':profile,
        'budget_left':budget_left,
    }
    return render(request,'home-with-profile.html',context)

def create_expenses(request):
    if request.method == "POST":
        form = CreateExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateExpenseForm()
    context={
        'form':form
    }
    return render(request,'expense-create.html',context)

def edit_expense(request,pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        form = EditExpenseForm(request.POST, request.FILES,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense':expense
    }
    return render(request,'expense-edit.html',context)

def delete_expense(request,pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense': expense
    }
    return render(request,'expense-delete.html',context)

def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()
    context = {
        'form':form,

    }
    return render(request,'home-no-profile.html',context)

def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(expense.price for expense in expenses)
    context = {
        'profile':profile,
        'expenses_count': len(expenses),
        'budget_left':budget_left,
    }
    return render(request, 'profile.html',context)

def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = EditProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form':form,
    }
    return render(request, 'profile-edit.html',context)

def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html',context)
