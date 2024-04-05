from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path("user_login/", views.loginuser, name='loginuser'),
    path("", login_required(views.Dashboard), name='UDashboard'),
    path("feedback/", login_required(views.feedback_view), name='Ufeedback'),
    path("senser_info/", login_required(views.Senser), name='Usenser_info'),
    path("gps/", login_required(views.Gps), name='Ugps'),
    path("reading/",login_required(views.Reading),name='Ureading'),
    path('signout/', views.signout, name='Usignout'),
    path('logout_success/', views.logout_success, name='Ulogout_success'),


]