from django.urls import path,include
from . import views

app_name = 'testapp'

urlpatterns = [
    path('posts/',views.PostView,name='post'),
    path('detail/<slug:slug>',views.PostDetail,name='detail'),
]
