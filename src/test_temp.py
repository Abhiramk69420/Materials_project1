from w1thermsensor import W1ThermSensor
import csv
import glob
import os
import time

DATA_FOLDER = "official_data"
TRIAL_DURATION = 30      # seconds
SAMPLE_INTERVAL = 3      # seconds

os.makedirs(DATA_FOLDER, exist_ok=True)

sensor = W1ThermSensor()

material = input("Enter material name: ").strip().lower()

existing_trials = glob.glob(
    os.path.join(DATA_FOLDER, f"{material}_trial*.csv")
)

trial_num = len(existing_trials) + 1

filename = os.path.join(
    DATA_FOLDER,
    f"{material}_trial{trial_num}.csv"
)

print(f"\nSaving data to {filename}")

start_time = time.time()

with open(filename, "w", newline="") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(["Time_s", "Temp_F"])

    while True:

        elapsed = time.time() - start_time

        if elapsed >= TRIAL_DURATION:
            break

        temp_c = sensor.get_temperature()
        temp_f = temp_c * 9 / 5 + 32

        writer.writerow([
            round(elapsed, 1),
            round(temp_f, 2)
        ])

        print(
            f"{elapsed:5.1f} s   {temp_f:6.2f} °F"
        )

        time.sleep(SAMPLE_INTERVAL)

print("\nTrial complete!")
print(f"Saved as {filename}")
