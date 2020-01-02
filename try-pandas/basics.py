import pandas as pd

print(pd.__version__)

df = pd.read_csv('./data/gapminder.tsv', sep='\t')
print(df.head())
print(df.info())

slice = df[['country', 'year', 'pop']]
print(slice.head())

just60s = df[(df.year >= 1960) & (df.year <= 1969)]
print(just60s.iloc[0:10, [0,2]])

print(df.year.min())
print(df.describe())

print(df['pop'].max())

print(df[df['pop'] == df['pop'].max()])

