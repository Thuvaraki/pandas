import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
from pandas.tseries.offsets import CustomBusinessDay

class MyBirthCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday("Thuva's birthday", month=4, day=12)
    ]

myc = CustomBusinessDay(calendar=MyBirthCalendar())
print(myc)

df = pd.date_range("4/1/2017","4/30/2017",freq=myc)
print(df)