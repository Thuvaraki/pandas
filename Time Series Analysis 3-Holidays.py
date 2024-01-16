import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

df = pd.read_csv("aapl_no_dates.csv")

usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())
rng = pd.date_range("7/1/2017", "7/21/2017", freq=usb)
df.set_index(rng, inplace=True)
print(df)
