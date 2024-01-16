import pandas as pd

df = pd.read_csv("aapl.csv", parse_dates=['Date'], index_col='Date')

# retrieving all data for january 2017
df_data = df.loc['2017-01']
print(df_data)

# retrieving all data for january 2017 of Close column
df_data_close = df.loc['2017-01'].Close
print(df_data_close)

df_data_close_mean = df.loc['2017-01'].Close.mean()
print(df_data_close_mean)

# retrieving data for particular date
print(df.loc["2017-01-03"])

# retrieving data within a range, should sort the index
df_sorted = df.sort_index()
df_slice = df_sorted.loc["2017-01-01":"2017-01-07"]
print(df_slice)


