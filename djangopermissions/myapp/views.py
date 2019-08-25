from django.shortcuts import render,redirect
from .models import Article
from .forms import UserLoginForm,PostCreate,SignupUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Permission
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

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
			return redirect(registersuccesfull)
	else:
		UserRegister = SignupUser()
	return render(request,'signup.html',{'UserRegister':UserRegister})

@login_required
def UserLogout(request):
	logout(request)
	return redirect(Userlogin)

def registersuccesfull(request):
	return render(request,'success.html')

@login_required
def userprofile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
		if (user == User.objects.get(username='anil')):
			user.has_perm('myapp.view_Article')
	else:
		user = request.user
	print(user)
	return render(request,'userprofile.html',{'user':user})

@login_required
def HomeView(request):
	return render(request,'home.html')

@login_required
def Create(request):
	if request.method == 'POST':
		postform = PostCreate(request.POST or None)
		if postform.is_valid():
			postform.save()
			redirect(ViewPost)
	else:
		postform = PostCreate()
	return render(request,'create.html',{'postform':postform})

@login_required
def ViewPost(request):
	post = Article.objects.all()
	return render(request,'viewpost.html',{'post':post})


	

