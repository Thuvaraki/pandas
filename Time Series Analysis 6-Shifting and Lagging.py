import pandas as pd

df = pd.read_csv("fb.csv",index_col='Date')
print(df)

# Shifting to the right-hand side (forward in time)
print(df.shift(1))
# Shifting to the left-hand side (backward in time)
print(df.shift(-1))

# creating a Prev Day Price column in df
df['Prev Day Price']=df['Price'].shift(1)
print(df)

df['1 Day change']=df['Price'] - df['Prev Day Price']
print(df)
