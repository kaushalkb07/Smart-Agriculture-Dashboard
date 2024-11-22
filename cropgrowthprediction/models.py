from django.db import models

class EnvironmentalData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    soil_moisture = models.FloatField()  # Moisture in percentage
    temperature = models.FloatField()   # Temperature in Celsius
    humidity = models.FloatField()      # Humidity in percentage

    def __str__(self):
        return f"{self.timestamp} - Moisture: {self.soil_moisture}%, Temp: {self.temperature}°C, Humidity: {self.humidity}%"

class Crop(models.Model):
    name = models.CharField(max_length=100)
    ideal_temperature = models.FloatField()  # Ideal temperature for the crop
    ideal_soil_moisture = models.FloatField()  # Ideal soil moisture for the crop
    growth_stages = models.JSONField(default=dict)  # Example: {"stage1": "Germination", "stage2": "Vegetative"}

    def __str__(self):
        return self.name
