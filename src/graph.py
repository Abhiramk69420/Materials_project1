import pandas as pd
import matplotlib.pyplot as plt
import glob

material = input("Enter material name: ").lower()

files = sorted(glob.glob(f"sample_data/{material}_trial*.csv"))

if len(files) == 0:
    print("No trial files found.")
    exit()

# Read all trial files
dataframes = [pd.read_csv(file) for file in files]

# Use the time column from the first trial
time = dataframes[0]["Time_s"]

# Combine all temperature columns
temps = pd.concat([df["Temp_F"] for df in dataframes], axis=1)

# Calculate average temperature
avg_temp = temps.mean(axis=1)

# Plot average curve
plt.figure(figsize=(8,5))
plt.plot(time, avg_temp, linewidth=2, label="Average Temperature")

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°F)")
plt.title(f"{material.capitalize()} Average Cooling Curve")
plt.grid(True)
plt.legend()

plt.savefig(f"sample_graphs/{material}_average_graph.png")
print(f"Graph saved as sample_graphs/{material}_average_graph.png")

plt.show()
