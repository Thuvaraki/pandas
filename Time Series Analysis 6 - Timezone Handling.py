import pandas as pd

df = pd.read_csv("msft.csv",header=1,index_col='Date Time',parse_dates=True)
print(df)
print(df.index) #Naive dateTime index

# Two types of DateTime Objects in Python
# 1. Naive (No timezone awareness)
# 2. Time zone aware datetime

# Converting naive DateTime index to Time zone aware datetime
df = df.tz_localize(tz='US/Eastern')
print(df.index)

df = df.tz_convert(tz='Europe/Berlin')
print(df)

# Use timezone in date_range() function
x = pd.date_range(start='16/01/2024',periods=5,freq='D',tz='Europe/London')
print(x)

# Use dateutil timezone
y = pd.date_range(start='16/01/2024',periods=5,freq='D',tz='dateutil/Europe/London')
print(y)