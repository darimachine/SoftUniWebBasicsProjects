from django import forms

from .models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username','email','age','password')
        widgets= {
            'password':forms.PasswordInput()
        }
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets= {
            'password':forms.PasswordInput()
        }
        labels = {
            'image': 'Profile Image',
        }

class ProfileDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        cars = Car.objects.all()
        cars.delete()
        return self.instance
    class Meta:
        model = Profile
        fields = ()
class CarCreateForm(forms.ModelForm):
    class Meta:
        model=Car
        fields ='__all__'
class CarEditForm(forms.ModelForm):
    class Meta:
        model=Car
        fields ='__all__'

class CarDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled']='disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
    class Meta:
        model=Car
        fields ='__all__'