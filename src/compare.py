import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
import glob

materials = input("Enter materials (example: aluminum,plastic,wood): ")
materials = materials.split(",")

plt.figure(figsize=(8,5))

print("\n===== Cooling Rate Results =====")

for m in materials:
    name = m.strip().lower()

    # Find all trial files
    files = sorted(glob.glob(f"sample_data/{name}_trial*.csv"))

    if len(files) == 0:
        print(f"No trial files found for {name}")
        continue

    # Read all trials
    dataframes = [pd.read_csv(file) for file in files]

    # Use the time values from the first trial
    time = dataframes[0]["Time_s"]

    # Average the temperatures
    temps = pd.concat([df["Temp_F"] for df in dataframes], axis=1)
    avg_temp = temps.mean(axis=1)

    # Plot average curve
    plt.plot(time, avg_temp, linewidth=2, label=name.capitalize())

    # Calculate average cooling rate
    start_temp = avg_temp.iloc[0]
    end_temp = avg_temp.iloc[-1]
    total_time = time.iloc[-1]

    rate = (start_temp - end_temp) / (total_time / 60)

    print(f"{name.capitalize()}: {rate:.2f} °F/min")

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°F)")
plt.title("Average Cooling Curve Comparison")
plt.legend()
plt.grid(True)

plt.savefig("official_graphs/comparison.png")
print("\nComparison graph saved to official_graphs/comparison.png")

plt.show()
