import pandas as pd

df = pd.read_csv("democsv.csv")

# drop all the rows which contain NaN values
print(df.dropna())

# drops rows that have fewer than 1 non-NaN value,
new_df = df.dropna(thresh=1)

# how='all' # Drop rows where all values are NaN
# if a row contain na value in only one column that row won't be deleted
new_df = df.dropna(how='all')

print(new_df)