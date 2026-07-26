import os
import glob
import pandas as pd
import numpy as np

DATA_FOLDER = "official_data"

materials = sorted(set(
    os.path.basename(file).split("_trial")[0]
    for file in glob.glob(os.path.join(DATA_FOLDER, "*_trial*.csv"))
))

print("\n========== ERROR ANALYSIS ==========\n")

results = []

for material in materials:

    files = sorted(
        glob.glob(
            os.path.join(DATA_FOLDER,
            f"{material}_trial*.csv")
        )
    )

    heating_rates = []

    for file in files:

        df = pd.read_csv(file)

        start = df["Temp_F"].iloc[0]
        end = df["Temp_F"].iloc[-1]
        total_time = df["Time_s"].iloc[-1]

        rate = (end - start)/(total_time/60)

        heating_rates.append(rate)

    heating_rates = np.array(heating_rates)

    mean = np.mean(heating_rates)

    std = np.std(
        heating_rates,
        ddof=1
    )

    stderr = std/np.sqrt(len(heating_rates))

    percent_uncertainty = (
        stderr/abs(mean)
    )*100 if mean != 0 else 0

    ci95 = 1.96*stderr

    print(material.capitalize())

    print(f"Mean Rate: {mean:.3f} °F/min")
    print(f"Standard Deviation: {std:.3f}")
    print(f"Standard Error: {stderr:.3f}")
    print(f"95% Confidence Interval: ±{ci95:.3f}")
    print(f"Percent Uncertainty: {percent_uncertainty:.2f}%")
    print()

    results.append({

        "Material": material.capitalize(),

        "Mean Heating Rate": round(mean,3),

        "Std Dev": round(std,3),

        "Std Error": round(stderr,3),

        "95% CI": round(ci95,3),

        "Percent Uncertainty": round(percent_uncertainty,2)

    })

pd.DataFrame(results).to_csv(
    os.path.join(
        DATA_FOLDER,
        "error_analysis.csv"
    ),
    index=False
)

print("Saved to official_data/error_analysis.csv")
