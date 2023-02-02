from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, CarCreateForm, CarEditForm, CarDeleteForm
from .models import Profile, Car


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None

def show_index(request):
    return render(request,'index.html')
def show_catalogue(request):
    cars = Car.objects.all()

    context ={
        'cars':cars,
        'total_cars':len(cars),
    }
    return render(request,'catalogue.html',context)
def create_profile(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()

    context={
        'form':form,
    }
    return render(request,'profile-create.html',context)
def profile_details(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price = sum(car.price for car in cars)
    context={
        'profile':profile,
        'total_price':total_price
    }
    return render(request,'profile-details.html',context)
def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)
def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = ProfileDeleteForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
def create_car(request):
    if request.method == "POST":
        form = CarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm()

    context={
        'form':form,
    }
    return render(request, 'car-create.html',context )
def car_details(request,pk):
    car = Car.objects.get(pk=pk)
    context={
        'car':car,
    }
    return render(request,'car-details.html',context)
def edit_car(request,pk):
    car = Car.objects.get(pk=pk)
    if request.method == "POST":
        form = CarEditForm(request.POST,request.FILES,instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarEditForm(instance=car)
    context={
        'form':form,
        'car':car,
    }
    return render(request,'car-edit.html',context)
def delete_car(request,pk):
    car = Car.objects.get(pk=pk)
    if request.method == "POST":
        form = CarDeleteForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarDeleteForm(instance=car)
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-delete.html', context)