# AV Performance Metrics Pipeline

This project demonstrates a simple Python-based pipeline for simulating and processing autonomous vehicle (AV) performance metrics. It includes calculating key metrics such as lane deviation, braking time, and stop time, which are essential for evaluating the behavior and performance of autonomous driving systems.

## Project Overview

The pipeline is designed to:

- Simulate AV sensor data, such as lane deviation, braking time, and stop time.
- Calculate important performance metrics based on the simulated data.
- Provide basic visualizations of the results to help analyze the performance.

## Key Features

- **Data Simulation**: Generates simulated AV data like lane deviation, braking time, and stop time.
- **Metrics Calculation**: Computes key performance metrics, including average lane deviation, braking time, and stop time.
- **Data Visualization**: Uses Python's `matplotlib` to visualize metrics.

## How to Run

You have two options to run this project:

### Option 1: Run in Google Colab (No Installation Needed)
[Click here to run this project in Google Colab](https://colab.research.google.com/drive/1UCg0FFqGo5ERxZpbF_EhIlYBL3_qMSAB?usp=sharing)

This will open the notebook in your browser where you can execute all the code cells without installing anything on your machine.

### Option 2: Run Locally (Manual Installation)

1. Clone this repository: https://github.com/alfredsilguero/av-performance-metrics-pipeline.
2. Navigate into the project folder:
cd av-performance-metrics-pipeline
3. Install dependencies: pip install -r requirements.txt
4. Run the script:
python main.py
