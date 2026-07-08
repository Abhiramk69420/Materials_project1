import os
import glob
import pandas as pd
import numpy as np

DATA_FOLDER = "official_data"

material = input("Enter material name: ").strip().lower()

files = sorted(glob.glob(
    os.path.join(DATA_FOLDER, f"{material}_trial*.csv")
))

if len(files) == 0:
    print(f"\nNo trial files found for '{material}'.")
    exit()

print("\n===== Trial Statistics =====")

max_temps = []
heating_rates = []
trial_lengths = []

for file in files:

    df = pd.read_csv(file)

    trial_lengths.append(len(df))

    start_temp = df["Temp_F"].iloc[0]
    end_temp = df["Temp_F"].iloc[-1]

    total_time = df["Time_s"].iloc[-1]

    max_temps.append(df["Temp_F"].max())

    # Heating rate (°F/min)
    rate = (end_temp - start_temp) / (total_time / 60)
    heating_rates.append(rate)

# ----------------------------
# Convert to numpy arrays
# ----------------------------

max_temps = np.array(max_temps)
heating_rates = np.array(heating_rates)

# ----------------------------
# Statistics
# ----------------------------

avg_max = np.mean(max_temps)
std_max = np.std(max_temps, ddof=1)
se_max = std_max / np.sqrt(len(max_temps))

avg_rate = np.mean(heating_rates)
std_rate = np.std(heating_rates, ddof=1)
se_rate = std_rate / np.sqrt(len(heating_rates))

confidence95 = 1.96 * se_rate

# ----------------------------
# Print Results
# ----------------------------

print(f"\nMaterial: {material.capitalize()}")

print(f"Trials: {len(files)}")

print(f"Average Maximum Temperature: {avg_max:.2f} °F")
print(f"Maximum Temperature Std Dev: {std_max:.2f} °F")

print(f"\nAverage Heating Rate: {avg_rate:.2f} °F/min")
print(f"Heating Rate Std Dev: {std_rate:.2f} °F/min")
print(f"Standard Error: {se_rate:.2f} °F/min")
print(f"95% Confidence Interval: ±{confidence95:.2f} °F/min")

print(f"\nShortest Trial Length: {min(trial_lengths)} samples")
print(f"Longest Trial Length: {max(trial_lengths)} samples")

# ----------------------------
# Save Summary
# ----------------------------

summary = pd.DataFrame({
    "Material": [material.capitalize()],
    "Trials": [len(files)],
    "Average_Max_Temp_F": [avg_max],
    "Max_Temp_StdDev": [std_max],
    "Average_Heating_Rate_F_per_min": [avg_rate],
    "Heating_Rate_StdDev": [std_rate],
    "Heating_Rate_SE": [se_rate],
    "Heating_Rate_95CI": [confidence95]
})

save_path = os.path.join(
    DATA_FOLDER,
    f"{material}_statistics.csv"
)

summary.to_csv(save_path, index=False)

print(f"\nStatistics saved to:\n{save_path}")
