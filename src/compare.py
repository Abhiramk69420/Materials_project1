import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt

materials = input("Enter materials (example: metal,plastic,wood): ")
materials = materials.split(",")

plt.figure()

for m in materials:
	name = m.strip()
	data = pd.read_csv(f"{name}_data.csv")
	plt.plot(data["Time_s"], data["Temp_F"], label=name)

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (F)")
plt.title("Cooling Curve Comparison")
plt.legend()
plt.grid()

print("\nCooling rate results:")

for m in materials:
	name = m.strip()
	data = pd.read_csv(f"{name}_data.csv")

	start_temp = data["Temp_F"].iloc[0]
	end_temp = data["Temp_F"].iloc[-1]
	total_time = data["Time_s"].iloc[-1]
	
	rate = (start_temp - end_temp) / (total_time/60)
	print(f"{name}: {rate:.2f} F per minute")

plt.savefig("comparison.png")
print("COMPARISON GRAPH CREATED")
