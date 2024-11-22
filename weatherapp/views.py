import requests
from django.shortcuts import render
from .forms import CityForm
from django.core.cache import cache
import requests
from django.shortcuts import render
from .forms import CityForm

def get_weather(request):
    url = "https://api.open-meteo.com/v1/forecast"
    weather_data = None
    error_message = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city'].strip().title()
            geocoding_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
            try:
                # Fetch coordinates from Nominatim
                geocoding_response = requests.get(geocoding_url, timeout=5)
                if geocoding_response.status_code == 200:
                    geo_data = geocoding_response.json()
                    if geo_data:
                        latitude = geo_data[0]['lat']
                        longitude = geo_data[0]['lon']
                    else:
                        raise Exception("Nominatim returned no results")
                else:
                    raise Exception("Nominatim service unavailable")
            except Exception:
                # Fallback to OpenCage
                opencage_api_key = "27df47907c7042ff8d09cf3b6617f0e8"
                opencage_url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={opencage_api_key}"
                try:
                    fallback_response = requests.get(opencage_url, timeout=5)
                    if fallback_response.status_code == 200:
                        geo_data = fallback_response.json().get('results')
                        if geo_data:
                            latitude = geo_data[0]['geometry']['lat']
                            longitude = geo_data[0]['geometry']['lng']
                        else:
                            error_message = f"City '{city}' not found using fallback."
                    else:
                        error_message = "Fallback geocoding service unavailable."
                except requests.exceptions.RequestException as e:
                    error_message = f"Error: {e}"

            # Fetch weather data from Open-Meteo
            if not error_message:
                params = {
                    'latitude': latitude,
                    'longitude': longitude,
                    'current_weather': 'true',
                }
                response = requests.get(url, params=params, timeout=5)
                if response.status_code == 200:
                    weather_data = response.json().get('current_weather')
                    weather_data['city'] = city
                else:
                    error_message = "Unable to fetch weather data. Please try again."

    else:
        form = CityForm()

    return render(request, 'weather/weatherapp.html', {
        'form': form,
        'weather_data': weather_data,
        'error_message': error_message,
    })
