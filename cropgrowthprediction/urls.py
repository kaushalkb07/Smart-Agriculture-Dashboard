from django.urls import path
from . import views

urlpatterns = [
    path('simulate-data/', views.simulate_environmental_data, name='simulate_data'),
    path('recommendations/<int:crop_id>/', views.get_recommendations, name='get_recommendations'),
]
