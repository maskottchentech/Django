from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('signup/', views.signupform,name='signup'),
    path('login/', views.Userlogin,name='login'),
    path('profile/', views.userprofile,name='profile'),
    path('home/', views.Homepage,name='home'),

    
    ]
