from django.urls import path
from . import views

urlpatterns = [
    path('Signup/', views.signupform,name='signup'),
    path('success/', views.success,name='success'),
]
