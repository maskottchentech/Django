from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import information
from .forms import problemform
from django.db.models import Q
from .filters import UserFilter


def indexpage(request):
    if request.method == 'POST':
        form = problemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(search)
    else:
        form = problemform()
    return render(request,'user.html',{'form':form})

    return render(req,'user.html')

#def newpage(request):
#    data = information.objects.all()
#    return render(request,'new.html',{'data': data})

def search(request):
    user_list = information.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    
    return render(request, 'search.html', {'filter': user_filter})





    