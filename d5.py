import pandas as pd

df = pd.read_csv("./Book1.csv")

print(df['temperature'].max())
print(df['temperature'].min())
print(df['temperature'].std())
print(df.describe())