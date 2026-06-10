import pandas as pd
import glob

results = []

files = glob.glob('data/*_average.csv')

for file in files:
    df = pd.read_csv(file)

    material = file.split('/')[-1].replace('_average.csv', '')

    max_temp = df['MaxTemp'].iloc[0]
    heating_rate = df['HeatingRate'].iloc[0]

    results.append({
        'Material': material.capitalize(),
        'HeatingRate': heating_rate,
        'MaxTemp': max_temp
    })

rankings = pd.DataFrame(results)

rankings['HeatingScore'] = (
    rankings['HeatingRate'] /
    rankings['HeatingRate'].max()
)

rankings['TemperatureScore'] = (
    rankings['MaxTemp'] /
    rankings['MaxTemp'].max()
)

rankings['OverallScore'] = (
    0.7 * rankings['HeatingScore'] +
    0.3 * rankings['TemperatureScore']
)

rankings = rankings.sort_values(
    by='OverallScore',
    ascending=False
)


rankings = rankings.reset_index(drop=True)
print(rankings[['Material', 'MaxTemp', 'HeatingRate', 'OverallScore']])
