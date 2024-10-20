from django.shortcuts import redirect, HttpResponse, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
def auth_dashboard(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('signin')

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def signin(request):
    return render(request, 'authenticate/login.html')

def signup(request):
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
            return redirect('signup')
        if password != password2:
            messages.error(request, 'Passwords must match')
            return redirect('signup')
        # Create User
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, 'User Created Successfully')
        return redirect('signin')  # Redirect to login after signup
    else:
        return HttpResponse('404 - Not Found')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # This logs the user in using session-based auth (optional)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('signin')
    else:
        # Capture the 'next' parameter in case it's passed in the GET request
        next_url = request.GET.get('next', '')
        return render(request, 'authenticate/login.html', {'next': next_url})

@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Loggedout Sucessfully')
    return redirect('auth_dashboard')

# Protected view that requires JWT authentication
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"message": "This is a protected view!", "user": request.user.username})

# Function to get tokens (you could use TokenObtainPairView from simplejwt as well)
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
