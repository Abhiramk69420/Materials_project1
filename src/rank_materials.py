import os
import glob
import pandas as pd
import numpy as np

DATA_FOLDER = "official_data"

print("\nFinding materials...")

# -----------------------------------
# Automatically find every material
# -----------------------------------

materials = sorted(set(
    os.path.basename(file).split("_trial")[0]
    for file in glob.glob(os.path.join(DATA_FOLDER, "*_trial*.csv"))
))

if len(materials) == 0:
    print("No trial files found.")
    exit()

results = []

# -----------------------------------
# Process each material
# -----------------------------------

for material in materials:

    files = sorted(
        glob.glob(
            os.path.join(DATA_FOLDER,
            f"{material}_trial*.csv")
        )
    )

    max_temps = []
    heating_rates = []

    for file in files:

        df = pd.read_csv(file)

        start_temp = df["Temp_F"].iloc[0]
        end_temp = df["Temp_F"].iloc[-1]
        total_time = df["Time_s"].iloc[-1]

        max_temps.append(df["Temp_F"].max())

        rate = (end_temp - start_temp) / (total_time / 60)
        heating_rates.append(rate)

    avg_max = np.mean(max_temps)
    avg_rate = np.mean(heating_rates)

    std_rate = np.std(heating_rates, ddof=1) if len(heating_rates) > 1 else 0

    score = (0.30 * avg_max) + (0.70 * avg_rate)

    results.append({
        "Material": material.capitalize(),
        "Trials": len(files),
        "Average Max Temp (°F)": round(avg_max,2),
        "Average Heating Rate (°F/min)": round(avg_rate,2),
        "Heating Rate Std Dev": round(std_rate,2),
        "Score": round(score,2)
    })

# -----------------------------------
# Create ranking
# -----------------------------------

ranking = pd.DataFrame(results)

ranking = ranking.sort_values(
    by="Score",
    ascending=False
).reset_index(drop=True)

ranking.index += 1

print("\n===== MATERIAL RANKINGS =====\n")
print(ranking)

# -----------------------------------
# Save results
# -----------------------------------

save_path = os.path.join(
    DATA_FOLDER,
    "material_rankings.csv"
)

ranking.to_csv(save_path)

print(f"\nRankings saved to:\n{save_path}")
