import os
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

DATA_FOLDER = "official_data"
GRAPH_FOLDER = "official_graphs"

os.makedirs(GRAPH_FOLDER, exist_ok=True)

materials = input(
    "Enter materials separated by commas (example: aluminum,plastic,wood): "
)

materials = [m.strip().lower() for m in materials.split(",")]

plt.figure(figsize=(10,6))

for material in materials:

    files = sorted(
        glob.glob(
            os.path.join(DATA_FOLDER, f"{material}_trial*.csv")
        )
    )

    if len(files) == 0:
        print(f"No data found for {material}.")
        continue

    # ------------------------
    # Read every trial
    # ------------------------

    dataframes = [pd.read_csv(file) for file in files]

    # ------------------------
    # Trim all trials to shortest length
    # ------------------------

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

    # ------------------------
    # Average + Standard Deviation
    # ------------------------

    avg_temp = temps.mean(axis=1)
    std_temp = temps.std(axis=1)

    # ------------------------
    # Normalize
    # ------------------------

    min_temp = avg_temp.min()
    max_temp = avg_temp.max()

    if max_temp != min_temp:
        avg_temp = (avg_temp - min_temp) / (max_temp - min_temp)
        std_temp = std_temp / (max_temp - min_temp)

    # ------------------------
    # Plot Average
    # ------------------------

    plt.plot(
        time,
        avg_temp,
        linewidth=2.5,
        label=material.capitalize()
    )

    # ------------------------
    # Plot Uncertainty Band
    # ------------------------

    plt.fill_between(
        time,
        avg_temp - std_temp,
        avg_temp + std_temp,
        alpha=0.20
    )

# ------------------------
# Graph Formatting
# ------------------------

plt.title(
    "Comparison of Average Temperature Response",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Time (seconds)",
    fontsize=12
)

plt.ylabel(
    "Normalized Temperature",
    fontsize=12
)

plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)

plt.legend(
    title="Materials"
)

plt.tight_layout()

save_path = os.path.join(
    GRAPH_FOLDER,
    "comparison_graph.png"
)

plt.savefig(
    save_path,
    dpi=300
)

print(f"\nComparison graph saved to:\n{save_path}")

plt.show()
