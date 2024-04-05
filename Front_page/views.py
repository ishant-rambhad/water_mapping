from django.http import HttpResponse
from django.shortcuts import render, redirect
from Admin.forms import RegistrationForm



def Frontpage(request):
    return render(request, 'Frontpage/Login.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Fregistration_success')
    else:
        form = RegistrationForm()
    return render(request, 'Frontpage/registration_form.html', {'form': form})


def registration_success(request):
    return render(request, 'Frontpage/registration_success.html')
