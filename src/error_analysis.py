import pandas as pd
import glob

files = glob.glob('data/*_average.csv')

for file in files:

    df = pd.read_csv(file)

    material = df['Material'].iloc[0]

    max_temp = df['MaxTemp'].iloc[0]

    heating_rate = df['HeatingRate'].iloc[0]

    print('\n' + material)

    print(f'Max Temperature: {max_temp:.2f} °F')
    print(f'Heating Rate: {heating_rate:.2f} °F/min')
