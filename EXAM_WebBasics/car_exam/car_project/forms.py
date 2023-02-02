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
