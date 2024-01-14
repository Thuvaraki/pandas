import pandas as pd

df = pd.read_csv("./Book1.csv")
print(df.index) #RangeIndex(start=0, stop=6, step=1)
print(df)
#           day  temperature  windspeed  event
# 0  01/01/2017           32          6   Rain
# 1  01/02/2017           35          7  Sunny
# 2  01/03/2017           28          2   Snow
# 3  01/04/2017           24          7   Snow
# 4  01/05/2017           32          4   Rain
# 5  01/06/2017           32          2  Sunny

print(df.set_index('day')) #setting the day as index, doesn't modify the original data frame, returns a new data frame
print(df.set_index('day' , inplace=True)) #inplace=True modify the original data frame
#             temperature  windspeed  event
# day
# 01/01/2017           32          6   Rain
# 01/02/2017           35          7  Sunny
# 01/03/2017           28          2   Snow
# 01/04/2017           24          7   Snow
# 01/05/2017           32          4   Rain
# 01/06/2017           32          2  Sunny
print(df.loc['01/05/2017']) #retrieving the data using the date index

df.reset_index(inplace=True) #resetting the index from day to integer
print(df)