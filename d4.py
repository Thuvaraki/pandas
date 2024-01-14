import pandas as pd

df = pd.read_csv("./Book1.csv")
# type of column event
print(type(df['event'])) #<class 'pandas.core.series.Series'>

# printing only event and day column
print(df[['event','day']])