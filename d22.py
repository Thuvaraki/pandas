import pandas as pd

temperature_df= pd.DataFrame({
    "city":["mumbai","delhi","banglore"],
    "temperature":[32,45,30],
},index=[0,1,2])

windspeed_df = pd.DataFrame({
    "city":["delhi","mumbai"],
    "windspeed":[7,12]
},index=[1,0]) #index is a way to align rows from different data frames

df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)
#        city  temperature    city  windspeed
# 0    mumbai           32  mumbai       12.0
# 1     delhi           45   delhi        7.0
# 2  banglore           30     NaN        NaN



# if we don't specify the index the output will be like
# #        city  temperature    city  windspeed
# # 0    mumbai           32   delhi        7.0
# # 1     delhi           45  mumbai       12.0
# # 2  banglore           30     NaN        NaN