from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),  # Include authentication app URLs
    path('dashboard/', include('dashboard.urls')),  # Include dashboard app URLs
    path('', lambda request: redirect('dashboard/', permanent=True)),  # Redirect root URL to dashboard
    path('weatherapp/', include('weatherapp.urls')),  # Include dashboard app URLs
    path('cropgrowthprediction/', include('cropgrowthprediction.urls')),  # Include crop growth prediction URLs
]
