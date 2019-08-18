from django.shortcuts import render,redirect
from .forms import SignupUser
from django.contrib.auth import authenticate,login

def signupform(request):
	if request.method == 'POST':
		form = SignupUser(request.POST or None)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect(HomeView)
	else:
		form = SignupUser()
	return render(request,'accounts/signup.html',{'form':form})

def HomeView(request):
	return render(request,'webpages/home.html')
