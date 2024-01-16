import pandas as pd

df = pd.read_excel("stocks.xlsx",header=(0,1))
print(df)

stacked = df.stack()
print(stacked)

unstacked = stacked.unstack()
print(unstacked)