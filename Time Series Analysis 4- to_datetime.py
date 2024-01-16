import pandas as pd

# print(pd.to_datetime(['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105']))

dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05','20170105']
print(pd.to_datetime(dt))

# European style dates with day first
print(pd.to_datetime('5-1-2016', dayfirst=True))

# Custom date time format
print(pd.to_datetime('2017$01$05', format='%Y$%m$%d'))

# Handling invalid dates
print(pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore'))
print(pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce'))


