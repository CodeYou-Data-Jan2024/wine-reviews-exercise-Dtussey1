import zipfile
import pandas as pd

df = pd.read_csv(r'wine-reviews-exercise-Dtussey1\data\winemag-data-130k-v2.csv.zip', compression='zip')

df['count'] = df.groupby('country')['country'].transform('count')

average_points = df.groupby('country')['points'].mean().round(1)

df = df.drop(columns=['Unnamed: 0', 'designation', 'points', 'description', 'price', 'province', 'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title', 'variety', 'winery'])

df = df.drop_duplicates('country')


df = df.merge(average_points.rename('points'), on= 'country')

print(df.to_string(index=False))

df.to_csv(r'wine-reviews-exercise-Dtussey1\data\reviews-per-country.csv')