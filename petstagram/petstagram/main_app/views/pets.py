from django.shortcuts import render, redirect

from ..forms import CreatePetForm
from ..helpers import get_profile
from ..models import PetPhoto, Pet


def create_pet(request):
    if request.method == "POST":
        pet_form = CreatePetForm(request.POST,instance=Pet(user_profile=get_profile()))
        if pet_form.is_valid():
            pet_form.save()
            return redirect('profile')
    else:
        pet_form = CreatePetForm()

    context={
        'pet_form':pet_form,
    }
    return render(request,'pet_create.html',context)

def edit_pet(request):
    return render(request,'pet_edit.html')

def delete_pet(request):
    return render(request,'pet_delete.html')