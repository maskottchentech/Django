from django.shortcuts import render,redirect
from .forms import PollForm
from django.http import HttpResponse


def pollpage(request):
	if request.method == 'POST':
		form = PollForm(request.POST or None)
		if form.is_valid():
			form.save()
			return HttpResponse("<h2>Succesfull</h2>")
			#return redirect()
	else:
		form = PollForm()
	return render(request,'poll.html',{'form':form})

def Thankyou(request):
	pass