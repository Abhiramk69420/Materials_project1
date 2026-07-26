import subprocess
import os

print("=" * 50)
print(" Materials Project Analysis Pipeline")
print("=" * 50)

while True:

    material = input(
        "\nEnter a material to analyze (or press Enter to finish): "
    ).strip().lower()

    if material == "":
        break

    print(f"\nGenerating graph for {material}...")
    subprocess.run(["python3", "src/graph.py"], input=f"{material}\n", text=True)

    print(f"\nCalculating statistics for {material}...")
    subprocess.run(["python3", "src/trial_statistics.py"], input=f"{material}\n", text=True)

print("\nGenerating comparison graph...")

materials = input(
    "\nEnter ALL materials separated by commas:\n"
)

subprocess.run(
    ["python3", "src/compare.py"],
    input=f"{materials}\n",
    text=True
)

print("\nRanking materials...")
subprocess.run(["python3", "src/rank_materials.py"])

print("\nRunning error analysis...")
subprocess.run(["python3", "src/error_analysis.py"])

print("\nDone!")
print("All graphs and statistics have been saved.")
