import pandas as pd
import glob

material = input('Enter material name: ').lower()

files = glob.glob(f'data/{material}_trial*.csv')

if len(files) == 0:
    print('No trial files found.')
    exit()

max_temps = []
heating_rates = []

for file in files:

    df = pd.read_csv(file)

    initial_temp = df['Temperature'].iloc[0]
    final_temp = df['Temperature'].iloc[-1]

    initial_time = df['Time'].iloc[0]
    final_time = df['Time'].iloc[-1]

    max_temp = df['Temperature'].max()

    time_minutes = (final_time - initial_time) / 60

    heating_rate = (
        final_temp - initial_temp
    ) / time_minutes

    max_temps.append(max_temp)
    heating_rates.append(heating_rate)

max_temp_series = pd.Series(max_temps)
heating_rate_series = pd.Series(heating_rates)

print('\n===== TRIAL STATISTICS =====\n')

print(f'Material: {material.capitalize()}')
print(f'Number of Trials: {len(files)}')

print('\nMax Temperature Statistics')
print(
    f'Average: {max_temp_series.mean():.2f} °F'
)
print(
    f'Std Dev: {max_temp_series.std():.2f} °F'
)

print('\nHeating Rate Statistics')
print(
    f'Average: {heating_rate_series.mean():.2f} °F/min'
)
print(
    f'Std Dev: {heating_rate_series.std():.2f} °F/min'
)

print(
    f'Uncertainty: ±{heating_rate_series.std() / (len(files)**0.5):.2f} °F/min'
)
