import pandas as pd
import glob

files = glob.glob('../data/*_average.csv')

for file in files:
    df = pd.read_csv(file)

    material = file.split('/')[-1].replace('_average.csv', '')

    initial_temp = df['Average Temperature'].iloc[0]
    final_temp = df['Average Temperature'].iloc[-1]

    initial_time = df['Time'].iloc[0]
    final_time = df['Time'].iloc[-1]

    time_minutes = (final_time - initial_time) / 60

    heating_rate = (final_temp - initial_temp) / time_minutes

    print(
        f'{material.capitalize():10} '
        f'{heating_rate:.2f} °F/min'
    )

