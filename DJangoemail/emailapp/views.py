from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignupForm

def Homepage(request):
	return render(request,'home.html')

def signup_view(request):
	subject = "Thank you for registering to our site"
	message = "You have succesfully created an account"
	email_from = settings.EMAIL_HOST_USER
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			recipient_list = [email,]
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			send_mail(subject,message,email_from,recipient_list)
			login(request,user)
			return redirect('app:home')
	else:
		form = SignupForm()
	return render(request,'signup.html',{'form':form})

