import random
import pandas as pd

# Set number of data points
num_data_points = 100

# Define realistic ranges for each environmental factor
soil_moisture_range = (20, 60)  # Soil moisture in percentage
temperature_range = (10, 35)    # Temperature in Celsius
humidity_range = (30, 80)       # Humidity in percentage

# Generate data
data = {
    "Soil_Moisture": [random.uniform(*soil_moisture_range) for _ in range(num_data_points)],
    "Temperature": [random.uniform(*temperature_range) for _ in range(num_data_points)],
    "Humidity": [random.uniform(*humidity_range) for _ in range(num_data_points)],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set display option to show all rows
pd.set_option('display.max_rows', None)

# Display the first few rows of the data
print(df)

# Save to a CSV file for further analysis if needed
# df.to_csv("simulated_sensor_data.csv", index=False)
