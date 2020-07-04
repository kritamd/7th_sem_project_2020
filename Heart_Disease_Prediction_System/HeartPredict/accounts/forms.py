from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput
        (
        attrs={'class':'form-control' , 'placeholder': 'Enter username'}
        ),
         required=True,max_length=50)

    email=forms.CharField(widget=forms.EmailInput
       (
        attrs={'class':'form-control' , 'placeholder':'Enter Email ID'}
       ),
        required=True,max_length=50)

    password=forms.CharField(widget=forms.PasswordInput
    (
        attrs={'class':'form-control' , 'placeholder':'Enter Password'}
    ),
    required=True,max_length=50)

    confirm_password=forms.CharField(widget=forms.PasswordInput
    (
        attrs={ 'class':'form-control', 'placeholder':'Confirm Password'}
    ),
    required=True,max_length=50)


    class Meta:
        model=User
        fields=('username','email','password')

    def clean(self):
        cleaned_data=super(UserForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password does not match')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('profile_pic',)

