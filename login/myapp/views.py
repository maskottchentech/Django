from django.shortcuts import render,redirect
from .forms import UserLoginForm,SignupUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Permission
from django.contrib.auth.decorators import login_required

def Userlogin(request):
	if request.method == 'POST':
		loginForm = UserLoginForm(request.POST or None)
		if loginForm.is_valid():
			username = loginForm.cleaned_data.get('username')
			password = loginForm.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user.is_active:
				login(request,user)
				return redirect(HomeView)
	else:
		loginForm = UserLoginForm()
	return render(request,'login.html',{'loginForm':loginForm})

def UserRegistration(request):
	if request.method == 'POST':
		UserRegister = SignupUser(request.POST or None)
		if UserRegister.is_valid():
			UserRegister.save()
			username = UserRegister.cleaned_data.get('username')
			password = UserRegister.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			return redirect(Userlogin)
	else:
		UserRegister = SignupUser()
	return render(request,'signup.html',{'UserRegister':UserRegister})

@login_required
def UserLogout(request):
	logout(request)
	return redirect(Userlogin)

@login_required
def userprofile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	print(user)
	return render(request,'userprofile.html',{'user':user})

def HomeView(request):
	return render(request,'home.html',{'form':form})