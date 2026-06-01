import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

material = input("Enter material name: ")
filename = f"{material}_data.csv"

data = pd.read_csv(filename)

print("Latest data:")
print(data.tail())

plt.clf()

plt.plot(data["Time_s"], data["Temp_F"])
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (F)")
plt.title("Materials Cooling Curve")
plt.grid()

plt.savefig("graph.png")
print("GRAPH SAVED")
plt.show()
