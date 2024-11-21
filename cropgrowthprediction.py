import numpy as np
import matplotlib.pyplot as plt

# Define environmental factor ranges
IDEAL_TEMP = (20, 30)  # in Celsius
IDEAL_HUMIDITY = (40, 70)  # in percentage
IDEAL_SOIL_MOISTURE = (30, 60)  # in percentage

# Simulated environmental data generator
def generate_environmental_data(days):
    np.random.seed(42)  # For reproducibility
    temperature = np.random.uniform(15, 35, days)  # Random temp range
    humidity = np.random.uniform(30, 80, days)     # Random humidity range
    soil_moisture = np.random.uniform(20, 70, days)  # Random soil moisture
    return temperature, humidity, soil_moisture

# Crop growth simulation function
def simulate_crop_growth(days):
    temperature, humidity, soil_moisture = generate_environmental_data(days)
    growth = []
    for t, h, s in zip(temperature, humidity, soil_moisture):
        temp_score = max(0, 1 - abs(t - np.mean(IDEAL_TEMP)) / (IDEAL_TEMP[1] - IDEAL_TEMP[0]))
        humidity_score = max(0, 1 - abs(h - np.mean(IDEAL_HUMIDITY)) / (IDEAL_HUMIDITY[1] - IDEAL_HUMIDITY[0]))
        soil_moisture_score = max(0, 1 - abs(s - np.mean(IDEAL_SOIL_MOISTURE)) / (IDEAL_SOIL_MOISTURE[1] - IDEAL_SOIL_MOISTURE[0]))
        
        # Weighted growth rate
        daily_growth = (temp_score + humidity_score + soil_moisture_score) / 3
        growth.append(daily_growth)
    return growth, temperature, humidity, soil_moisture

# Plotting function
def plot_growth(days, growth, temperature, humidity, soil_moisture):
    plt.figure(figsize=(12, 6))
    
    # Crop growth
    plt.subplot(2, 1, 1)
    plt.plot(range(days), np.cumsum(growth), label='Cumulative Growth', color='green')
    plt.title('Crop Growth Simulation')
    plt.xlabel('Day')
    plt.ylabel('Growth Stage')
    plt.legend()
    plt.grid(True)
    
    # Environmental factors
    plt.subplot(2, 1, 2)
    plt.plot(range(days), temperature, label='Temperature (°C)', color='red')
    plt.plot(range(days), humidity, label='Humidity (%)', color='blue')
    plt.plot(range(days), soil_moisture, label='Soil Moisture (%)', color='brown')
    plt.title('Environmental Factors')
    plt.xlabel('Day')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    # Save the plot as an image file
    plt.savefig("crop_growth_simulation.png")
    print("Plot saved as 'crop_growth_simulation.png'")


# Run the simulation
days = 100  # Number of days to simulate
growth, temperature, humidity, soil_moisture = simulate_crop_growth(days)
plot_growth(days, growth, temperature, humidity, soil_moisture)