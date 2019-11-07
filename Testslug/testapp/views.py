from django.shortcuts import render
from django.http import HttpResponse
from .models import PostData

def PostView(request):
	posts = PostData.objects.all()
	return render(request,'home.html',{'posts':posts})
	

def PostDetail(request,slug):
	detail = PostData.objects.filter(slug=slug)

	if detail.exists():
		detail = detail.first()
	else:
		return HttpResponse("<h3>Page Not Found</h3")
	return render(request,'detail.html',{'detail':detail})
