import zipfile
import pandas as pd

df = pd.read_csv(r'data\winemag-data-130k-v2.csv.zip', compression='zip')

df['count'] = df.groupby('country')['country'].transform('count')

df2 = df.drop(columns=['Unnamed: 0', 'description', 'price', 'province', 'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title', 'variety', 'winery'])

df3 = df2.drop_duplicates('country')

average_points = df3['points'].mean()

df3['points'] = round(average_points, 1)

df3 = df3[['country', 'count', 'points']]

print(df3.to_string(index=False))

df3.to_csv(r'data\reviews-per-country.csv')