import datetime

from django import forms

from .models import Profile, PetPhoto, Pet


class BootstrapFormMixin:
    fields={}
    def _init_bootstrap_form_controls(self):
        for _ , field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget,'attrs',{})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class']=''
            field.widget.attrs['class']+=' form-control'
class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_bootstrap_form_controls()
    class Meta:
        model=Profile
        fields = ('first_name','last_name','picture')
        widgets={
            'first_name': forms.TextInput(
                attrs={
                    'placeholder':'Enter first name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }),
        }

class EditProfileForm(BootstrapFormMixin,forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }),
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'Enter email'
                }),
            'description':forms.Textarea(
                attrs={
                    'placeholder':'Enter description',
                    'rows':3,
                }),
            'date_of_birth':forms.DateInput(
                attrs={
                    'type':'date',
                    'min':'1920-01-01',
                    'max':datetime.date.today()

                }
            )


        }
class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        pets = self.instance.pet_set.all() # self.instance e PROFILA
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

        return self.instance
    class Meta:
        model = Profile
        fields = ()

class CreatePetForm(BootstrapFormMixin,forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_bootstrap_form_controls()
    class Meta:
        model = Pet
        fields = ('name','type','date_of_birth')
        widgets={
            'name':forms.TextInput(
                attrs={
                    'placeholder':'Enter pet name'
                }),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': '1920-01-01',
                    'max': datetime.date.today()

                }
            )

        }
