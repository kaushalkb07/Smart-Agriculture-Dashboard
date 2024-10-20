from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .import views
from .views import ProtectedView

 # URL for signup
urlpatterns = [
    path('', views.auth_dashboard, name='auth_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    # Endpoint to obtain JWT token (login)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Endpoint to refresh JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Protected endpoint
    path('api/protected/', ProtectedView.as_view(), name='protected'),
 ]