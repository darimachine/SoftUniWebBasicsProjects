import os

from django import forms

from .models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget','first_name','last_name','image')
        labels ={
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image':'Profile Image',
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget','first_name','last_name','image')

class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if self.instance.image.name !='':
            image_path = self.instance.image.path
        self.instance.delete()
        Expense.objects.all().delete()
        if self.instance.image.name != '':
            os.remove(image_path)
        return self.instance
    class Meta:
        model = Profile
        fields = ()

class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields =('title','description','image','price')
class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields =('title','description','image','price')
class DeleteExpenseForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for _,field in self.fields.items():
            field.widget.attrs['readonly']='readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
    class Meta:
        model = Expense
        fields =('title','description','image','price')



