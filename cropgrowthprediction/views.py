from django.shortcuts import render
from django.http import JsonResponse
from .models import EnvironmentalData, Crop
import random

def simulate_environmental_data(request):
    # Generate random environmental data
    soil_moisture = random.uniform(10, 50)  # Simulated moisture percentage
    temperature = random.uniform(15, 35)   # Simulated temperature in °C
    humidity = random.uniform(30, 80)      # Simulated humidity percentage

    # Save data to the database
    env_data = EnvironmentalData.objects.create(
        soil_moisture=soil_moisture,
        temperature=temperature,
        humidity=humidity,
    )

    return JsonResponse({
        'message': 'Environmental data simulated successfully.',
        'data': {
            'soil_moisture': soil_moisture,
            'temperature': temperature,
            'humidity': humidity,
        }
    })

def get_recommendations(request, crop_id):
    try:
        crop = Crop.objects.get(id=crop_id)
        latest_env_data = EnvironmentalData.objects.last()

        if not latest_env_data:
            return JsonResponse({'error': 'No environmental data found.'}, status=404)

        recommendations = []
        if latest_env_data.soil_moisture < crop.ideal_soil_moisture:
            recommendations.append("Irrigation needed: Soil moisture is low.")
        if latest_env_data.temperature < crop.ideal_temperature:
            recommendations.append("Consider heating: Temperature is below ideal conditions.")
        if latest_env_data.temperature > crop.ideal_temperature:
            recommendations.append("Consider cooling: Temperature is above ideal conditions.")

        return JsonResponse({
            'crop': crop.name,
            'recommendations': recommendations,
            'environmental_data': {
                'soil_moisture': latest_env_data.soil_moisture,
                'temperature': latest_env_data.temperature,
                'humidity': latest_env_data.humidity,
            }
        })
    except Crop.DoesNotExist:
        return JsonResponse({'error': 'Crop not found.'}, status=404)

