from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin_login/', views.loginadmin, name='loginadmin'),
    path("", login_required(views.Dashboard), name='Dashboard'),
    path("feedback/", login_required(views.feedback_view), name='feedback'),
    path("senser_info/", login_required(views.Senser), name='senser_info'),
    path("tables/", login_required(views.display_feedback), name='tables'),
    path("gps/", login_required(views.Gps), name='gps'),
    path("reading/",login_required(views.Reading),name='reading'),
    path("feedback/display/", login_required(views.display_feedback), name="display_feedback"),
    path("registration/", login_required(views.registration), name="registration"),
    path('registration_data/', views.registration_info, name='registration_info'),
    path('registration/success/', login_required(views.registration_success), name='registration_success'),
    path('signout/', views.signout, name='signout'),
    path('logout_success/', views.logout_success, name='logout_success'),
]
