import pandas as pd

temperature_df= pd.DataFrame({
    "city":["mumbai","delhi","banglore"],
    "temperature":[32,45,30],
},index=[0,1,2])

s = pd.Series(['Humid','Dry','Rain'],name="event")
print(s)
# output
# 0    Humid
# 1      Dry
# 2     Rain
# Name: event, dtype: object

df = pd.concat([temperature_df,s],axis=1)
print(df)
#        city  temperature  event
# 0    mumbai           32  Humid
# 1     delhi           45    Dry
# 2  banglore           30   Rain