# main.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate some AV performance metrics (simple example)
data = {
    'lane_deviation': np.random.normal(0.5, 0.1, 100),  # Average lane deviation, std dev
    'braking_time': np.random.normal(2.0, 0.5, 100),    # Braking time in seconds
    'stop_time': np.random.normal(1.5, 0.4, 100),       # Stop time in seconds
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the average of each metric
avg_lane_deviation = df['lane_deviation'].mean()
avg_braking_time = df['braking_time'].mean()
avg_stop_time = df['stop_time'].mean()

# Print the results
print("AV Performance Metrics:")
print(f"avg_lane_deviation: {avg_lane_deviation:.2f}")
print(f"avg_braking_time: {avg_braking_time:.2f}")
print(f"avg_stop_time: {avg_stop_time:.2f}")

# Visualize the results (optional)
df.plot(kind='hist', bins=10, alpha=0.5, title="AV Performance Metrics Distribution")
plt.show()
