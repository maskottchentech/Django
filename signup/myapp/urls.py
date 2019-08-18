from django.urls import path
from . import views

urlpatterns = [
    path('Signup/', views.signupform,name='signup'),
    path('home/', views.HomeView,name='home'),
]
