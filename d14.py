import pandas as pd

# converting the type of day column(str) to timestamp
# parse_dates=["day"]: This part of the code specifies that the "day" column in the DataFrame
# should be parsed as dates. This means that pandas will attempt to convert the values in the
# "day" column to datetime objects.
df = pd.read_csv("Book1.csv",parse_dates=["day"])
df.set_index('day',inplace=True) #setting day column as index

# print(type(df.day[0]))   #<class 'pandas._libs.tslibs.timestamps.Timestamp'>
print(df)