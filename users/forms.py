from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Form for user registration
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()  								#Allows users to register their emails (only specific to this form)

	class Meta:
		model=User
		fields=['username','email','password1','password2'] #Other fields to be included and filled in this form

#Allow users to update their information (Username and email id in this case)
class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']

#Allows users to update their profile picture
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']
			