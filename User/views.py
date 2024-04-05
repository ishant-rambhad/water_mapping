from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from Admin.models import QuickFormData
from Admin.forms import QuickForm
from Admin.models import Enquiry,FeedbackData
from django.http import HttpResponse


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Admin.models import Registration

# def authenticate_admin_registration(name, password):
#     print(name,password)
#     try:
#         # Query the Admin Registration table for the user with the given username
#         print(Registration.objects.all())
#         user = Registration.objects.get(name=name)
#         print(user)
#         print("1")
#         # Check if the password matches
#         if user.check_password(password):
#             print("2")
#             return user
#         else:
#             print("3")
#             return None
#     except Exception as e:
#         return e

def authenticate_admin_registration(name, password):
    try:
        # Query the Admin Registration table for the user with the given username
        print(Registration.objects.get(name=name))
        user = Registration.objects.get(name=name)

        # Check if the password matches using Django's check_password function
        if check_password(password, user.password):
            return user
        else:
            return None
    except Exception as e:
        return e

# views.py
from Admin.models import Registration

def fetch_data():
    print("1")
    print(Registration.objects.all())
    # Query the database to fetch all records from the YourModel table
    registrations = Registration.objects.all()
    print("1")
    # You can perform additional filtering or manipulation here if needed
    print(registrations)
    print("1")

    return registrations


def loginuser(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user against the Admin Registration table
        # fetch_data()
        print("2")
        user = authenticate_admin_registration(name, password)
        print("2")

        if user is not None:
            # Authentication successful, log the user in.
            login(request, user)
            return redirect('UDashboard')
        else:
            # Authentication failed, display an error message.
            error_message = "Invalid username or password. Please try again."
            return render(request, 'user/login_error.html', {'error_message': error_message})

    # If it's not a POST request or if authentication fails, show the login form.
    return render(request, 'user/user_login.html')


# from django.contrib.auth import authenticate, login
# from Admin.models import Registration  # Import the model for Admin_registration

# def loginuser(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Query the Admin_registration table for the user
#         user = authenticate_admin_registration(username=username, password=password)
        
#         if user is not None:
#             # Authentication successful, log the user in.
#             print(login(request, user))
#             login(request, user)
#             return redirect('UDashboard')
#         else:
#             # Authentication failed, display an error message.
#             error_message = "Invalid username or password. Please try again."
#             return render(request, 'user/login_error.html', {'error_message': error_message})

#     # If it's not a POST request or if authentication fails, show the login form.
#     return render(request, 'user/user_login.html')

# def authenticate_admin_registration(username, password):
#     try:
#         # Query the Admin_registration table for the user with the given username
#         user = Registration.objects.get(username=username)
        
#         # Check if the password matches
#         if user.check_password(password):
#             return user
#         else:
#             return None
#     except Registration.DoesNotExist:
#         return None

# Create your views here.

# def loginuser(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         context={
#             "user_name": username
#         }

#         if user is not None:
#             # Authentication successful, log the user in.
#             login(request, user)
#             return redirect('UDashboard')
#         else:
#             # Authentication failed, display an error message.
#             error_message = "Invalid username or password. Please try again."
#             return render(request, 'user/login_error.html', {'error_message': error_message})

#     # If it's not a POST request or if authentication fails, show the login form.
#     return render(request, 'user/user_login.html')


@login_required
def Dashboard(request):
    if request.method == 'POST':
        form = QuickForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UDashboard')  # Redirect to the same page after submission
    else:
        form = QuickForm()

    quick_form_data = QuickFormData.objects.all()

    return render(request, 'user/user_Dash.html', {'form': form, 'quick_form_data': quick_form_data})


@login_required
def Senser(request):
    return render(request, "user/ui-elements.html")

@login_required
def Table(request):
    return render(request, "user/tables.html")

@login_required
def Gps(request):
    return render(request, "user/presentations.html")

# @login_required
# def Registration(request):
#     return render(request, "user/Registration_form.html")

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
        return render(request, 'user/forms.html')

@login_required
def Reading(request):
    return render(request, "user/reading.html")


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
    template_name='user/logout_success.html',
    next_page='Frontpage'  # Redirect to the login page after logout.
)


