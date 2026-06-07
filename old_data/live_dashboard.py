import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import time

plt.ion()

print("Live dashboard running... press CTRL + C to stop")

while True:
	try:
		data = pd.read_csv("temp_data.csv")
		
		plt.clf()
		plt.plot(data["Time_s"], data["Temp_F"])
		plt.xlabel("Time (seconds)")
		plt.ylabel("Temp (F)")
		plt.title("Live Temperature Dashboard")
		plt.grid()

		plt.pause(2)
	except:
		pass
