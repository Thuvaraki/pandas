import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
from pandas.tseries.offsets import CustomBusinessDay

class MyBirthCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday("Thuva's birthday", month=4, day=15,observance=nearest_workday)
    #    15  -saturday and 16-sunday so the nearest_workday => 14 is a holiday
    ]

myc = CustomBusinessDay(calendar=MyBirthCalendar())
print(myc)

df = pd.date_range("4/1/2017","4/30/2017",freq=myc)
print(df)