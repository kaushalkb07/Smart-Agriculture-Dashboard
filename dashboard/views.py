from django.shortcuts import redirect, HttpResponse, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
def auth_dashboard(request):
    print("User authenticated:", request.user.is_authenticated)  # Debug line
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if authenticated
    else:
        return redirect('user_login')  # Redirect to user login page
    
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def user_login(request):
    return render(request, 'authenticate/login.html')

def user_signup(request):
    return render(request, 'authenticate/signup.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # Validation Checking
        if not (1 <= len(username) <= 10):
            messages.error(request, 'Username must be between 1 and 10 characters')
            return redirect('user_signup')
        if password != password2:
            messages.error(request, 'Passwords must match')
            return redirect('user_signup')
        # Create User
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, 'User Created Successfully')

        return redirect('user_login')  # Redirect to login after signup
    else:
        return HttpResponse('404 - Not Found')
    
def signin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('user_login')
    else:
        return redirect('user_login')

@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Loggedout Sucessfully')
    return redirect('auth_dashboard')

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": "This is a protected view!", "user": request.user.username})
