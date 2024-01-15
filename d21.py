import pandas as pd

temperature_df= pd.DataFrame({
    "city":["mumbai","delhi","banglore"],
    "temperature":[32,45,30],
})

windspeed_df = pd.DataFrame({
    "city":["mumbai","delhi","banglore"],
    "windspeed":[7,12,9]
})

df = pd.concat([temperature_df,windspeed_df])
print(df)
#        city  temperature  windspeed
# 0    mumbai         32.0        NaN
# 1     delhi         45.0        NaN
# 2  banglore         30.0        NaN
# 0    mumbai          NaN        7.0
# 1     delhi          NaN       12.0
# 2  banglore          NaN        9.0

df = pd.concat([temperature_df,windspeed_df],axis=1) #axis=1 appends data as column
print(df)
#        city  temperature      city  windspeed
# 0    mumbai           32    mumbai          7
# 1     delhi           45     delhi         12
# 2  banglore           30  banglore          9