from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#Creating an account on the website
def register(request):
	
	if request.method=="POST":
	
		form=UserRegisterForm(request.POST)
		
		#Checks validity of the form. If valid, saves the response in the database (new user created!).
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}')
			return redirect('login')
	
	else:
		form=UserRegisterForm()

	return render(request,'users/register.html',{'form':form})

#View for the user to update their profile details (username, email id and profile picture). 
#Requires the user to be logged in
@login_required
def profile(request):
	
	if request.method=='POST':
		
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

		#Saves the response if the form is valid (user form and profile form).
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Details updated')
			return redirect('profile')

	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)
	
	context={
		'u_form':u_form,
		'p_form':p_form
	}
	
	return render(request,'users/profile.html',context)
