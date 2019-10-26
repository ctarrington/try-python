import pandas as pd

print(pd.__version__)

df = pd.read_csv('./data/gapminder.tsv', sep='\t')
print(df.head())


