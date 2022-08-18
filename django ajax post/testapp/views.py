from django.shortcuts import render
from .forms import ContactForm
from django.http import JsonResponse

def readval(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['message'])
            return JsonResponse({"response":"success"}, status=200)


def index(request):
    
    form = ContactForm()
    return render(request,'index.html',{'form':form})

def index1(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name']) 
            print(form.cleaned_data['email']) 
            print(form.cleaned_data['message']) 
    else:
        form = ContactForm()
    return render(request,'index1.html',{'form':form})

