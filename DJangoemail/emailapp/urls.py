from django.urls import path
from . import views
app_name = 'app'
urlpatterns = [
 
    path('signup/',views.signup_view, name='signup'),
    path('home/',views.Homepage,name='home' ),
]