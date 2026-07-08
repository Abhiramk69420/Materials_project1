import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

DATA_FOLDER = "official_data"
GRAPH_FOLDER = "official_graphs"

os.makedirs(GRAPH_FOLDER, exist_ok=True)

material = input("Enter material name: ").strip().lower()

files = sorted(glob.glob(
    os.path.join(DATA_FOLDER, f"{material}_trial*.csv")
))

if len(files) == 0:
    print(f"\nNo trial files found for '{material}'.")
    exit()

print(f"\nFound {len(files)} trial(s).")

# --------------------------
# Read all trial files
# --------------------------

dataframes = [pd.read_csv(file) for file in files]

# --------------------------
# Trim to shortest trial
# --------------------------

min_len = min(len(df) for df in dataframes)

trimmed = [
    df.iloc[:min_len].reset_index(drop=True)
    for df in dataframes
]

time = trimmed[0]["Time_s"]

temps = pd.concat(
    [df["Temp_F"] for df in trimmed],
    axis=1
)

avg_temp = temps.mean(axis=1)
std_temp = temps.std(axis=1)

# --------------------------
# Plot
# --------------------------

plt.figure(figsize=(8,5))

plt.plot(
    time,
    avg_temp,
    color="blue",
    linewidth=2,
    label="Average Temperature"
)

plt.fill_between(
    time,
    avg_temp - std_temp,
    avg_temp + std_temp,
    alpha=0.2,
    label="±1 SD"
)

plt.title(f"{material.capitalize()} Temperature Curve")
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°F)")
plt.grid(True)
plt.legend()

save_path = os.path.join(
    GRAPH_FOLDER,
    f"{material}_average_graph.png"
)

plt.savefig(save_path, dpi=300)

print(f"\nGraph saved to:\n{save_path}")

plt.show()
