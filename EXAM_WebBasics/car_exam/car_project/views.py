from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from .models import Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None

def show_index(request):
    return render(request,'index.html')
def show_catalogue(request):
    return render(request,'catalogue.html')
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
    context={
        'profile':profile,
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
    pass
def car_details(request):
    pass
def edit_car(request):
    pass
def delete_car(request):
    pass