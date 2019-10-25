from django.shortcuts import render
from .forms import formdata



def base(request):
	return render(request,'base.html')


def home(request):
	return render(request,'home.html')	


def about(request):
	return render(request,'about.html')


def contact(request):
	return render(request,'contact.html')

def c(request):
	if request.method == 'POST':
		form = formdata(request.POST)
		if form.is_valid():
			print(form)
			form.save(commit=True)
	else:
		form = formdata()

	return render(request,'c.html',{'form':form})


# Create your views here.
