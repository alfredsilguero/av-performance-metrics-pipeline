import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate AV sensor data
def generate_sensor_data(n=100):
    np.random.seed(0)
    data = {
        "lane_deviation": np.random.normal(0, 0.5, n),  # Simulating lane deviation (in meters)
        "braking_time": np.random.normal(2, 0.2, n),    # Simulating braking time (in seconds)
        "stop_time": np.random.normal(1.5, 0.1, n),     # Simulating stop time (in seconds)
    }
    return pd.DataFrame(data)

# Calculate key AV performance metrics
def calculate_metrics(df):
    metrics = {
        "avg_lane_deviation": df["lane_deviation"].abs().mean(),
        "avg_braking_time": df["braking_time"].mean(),
        "avg_stop_time": df["stop_time"].mean(),
    }
    return metrics

# Plot some of the metrics
def plot_metrics(df):
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.hist(df["lane_deviation"], bins=20, color='blue', alpha=0.7)
    plt.title("Lane Deviation Histogram")

    plt.subplot(1, 2, 2)
    plt.hist(df["braking_time"], bins=20, color='red', alpha=0.7)
    plt.title("Braking Time Histogram")
    plt.tight_layout()
    plt.show()

# Main function to run the pipeline
def main():
    data = generate_sensor_data(1000)  # Generate 1000 data points
    metrics = calculate_metrics(data)
    print("AV Performance Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")

    plot_metrics(data)

if __name__ == "__main__":
    main()
