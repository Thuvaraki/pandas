import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay

myc = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu')
df = pd.date_range("7/1/2017","7/29/2017",freq=myc)
print(df)