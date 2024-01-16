import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aapl.csv", parse_dates=['Date'], index_col='Date')

# df.Close: This selects the 'Close' column from your DataFrame df.
# .resample('M'): This is a time-based operation that allows to change the frequency of time series data.
# In this case, you are resampling it to a monthly frequency ('M').
# .mean(): After resampling, you are applying the mean function to calculate the mean value for each month.
resampled_df = df.Close.resample('M').mean()
print(resampled_df)

# Plot the resampled DataFrame
resampled_df.plot()
plt.show()

# drawing br chart
resampled_df.plot(kind="bar")
plt.show()