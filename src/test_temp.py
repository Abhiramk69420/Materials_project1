from w1thermsensor import W1ThermSensor
import time
import csv
import glob

sensor = W1ThermSensor()

material = input("Enter material name: ").lower()

existing_trials = glob.glob(f"official_data/{material}_trial*.csv")
print(existing_trials)

print(len(existing_trials))

trial_num = len(existing_trials) + 1

filename = f"official_data/{material}_trial{trial_num}.csv"

print(f"Saving data to {filename}")

start = time.time()

try:
    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Time_s", "Temp_F"])

        while True:

            temp_c = sensor.get_temperature()

            temp_f = (temp_c * 9/5) + 32

            current_time = time.time() - start

            writer.writerow([
                round(current_time, 2),
                round(temp_f, 2)
            ])

            print(
                f"{round(current_time,1)}s | "
                f"{temp_f:.2f}°F"
            )

            time.sleep(2)

except KeyboardInterrupt:
    print("\nData collection stopped.")
