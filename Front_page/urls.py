from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Frontpage, name='Frontpage'),
    path("registration/", views.registration, name="Fregistration"),
    path('registration/success/', views.registration_success, name='Fregistration_success'),

]