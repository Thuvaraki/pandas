import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aapl_no_dates.csv")

# Create a date range
# freq='B' exclude the weekend
# if freq='D' weekends also will be included
rng = pd.date_range(start="6/1/2017",end="6/30/2017",freq="B")
print(rng)

df.set_index(rng,inplace=True)

df.Close.plot()
plt.show()

# include weekends also
# if freq='D' weekends also will be included
# method='pad': used to fill missing values.if there is a missing value for a specific date, it will be filled with
# the value from the previous available date
pad_D_df = df.asfreq('D',method='pad')
print(pad_D_df)

# Hourly data
pad_H_df = df.asfreq('H',method='pad')
print(pad_H_df)

# Weekly data
pad_W_df = df.asfreq('W',method='pad')
print(pad_W_df)

# retrieving data from partial date range
x = df.loc['2017-06-01':'2017-06-10']
print(x)

##############
range=pd.date_range(start="1/1/2017",freq='H',periods=5)
print(range)
