from django.urls import path
from  . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
 
path('Login/',views.login_view , name='login'),
path('Logout/',views.log_out,name='logout')
]