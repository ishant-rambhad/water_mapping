from django.shortcuts import render
from .models import Enquiry,FeedbackData
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import QuickFormData
from .forms import QuickForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse



def loginadmin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print(user)
        context={
            "admin_name": username
        }

        if user is not None:
            # Authentication successful, log the user in.
            login(request, user)
            return redirect('Dashboard')
        else:
            # Authentication failed, display an error message.
            error_message = "Invalid username or password. Please try again."
            return render(request, 'admin/login_error.html', {'error_message': error_message})

    # If it's not a POST request or if authentication fails, show the login form.
    return render(request, 'admin/admin_login.html')

@login_required
def Dashboard(request):
    num_rows = fetch_row()
    if request.method == 'POST':
        form = QuickForm(request.POST)
        if form.is_valid():
            form.save()
            num_rows = fetch_row()

            return redirect('Dashboard')  # Redirect to the same page after submission
    else:
        form = QuickForm()

    quick_form_data = QuickFormData.objects.all()

    return render(request, 'admin/admin_page.html', {'form': form, 'quick_form_data': quick_form_data,'num_rows': num_rows})

@login_required
def Senser(request):
    return render(request, "admin/ui-elements.html")

@login_required
def Table(request):
    return render(request, "admin/tables.html")

@login_required
def Gps(request):
    return render(request, "admin/presentations.html")

@login_required
def Registration(request):
    return render(request, "admin/Registration_form.html")

@login_required
def feedback_view(request):  # Changed the name of the view function
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        # Convert "on" to True, None otherwise
        check_me_out = request.POST.get('check_me_out') == 'on'

        feedback_text = request.POST.get('feedback_text')

        enquiry = Enquiry.objects.create(
            name=name,
            email=email,
            address=address,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            check_me_out=check_me_out,
            feedback_text=feedback_text
        )

        return HttpResponse("Form submitted successfully")
    else:
        print("2")
        return render(request, 'admin/forms.html')

@login_required
def Reading(request):
    return render(request, "admin/reading.html")

@login_required
def display_feedback(request):
    feedback_data = Enquiry.objects.all()  # Retrieve all feedback entries from the database
    return render(request, 'admin/display_feedback.html', {'feedback_data': feedback_data})



def logout_success(request):
    return render(request, 'admin/logout_success.html')



@login_required
def signout(request):
    # Log the user out using Django's built-in logout function.
    logout(request)
    # Redirect to a page to display a logout success message.
    return redirect('logout_success')

# You can use the built-in LogoutView for the success message.
logout_success = LogoutView.as_view(
    template_name='admin/logout_success.html',
    next_page='Frontpage'  # Redirect to the login page after logout.
)


@login_required
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'admin/registration_form.html', {'form': form})

@login_required
def registration_success(request):
    return render(request, 'admin/registration_success.html')


from .models import Registration

def fetch_row():
# Fetch all records from the MyModel table
    queryset = Registration.objects.all()

# Get the length of the queryset (number of rows)
    num_rows = queryset.count()
    print(num_rows)
    return num_rows

def registration_info(request):
    registrations = Registration.objects.all()
    return render(request, 'admin/registration_info.html', { 'registrations': registrations})
