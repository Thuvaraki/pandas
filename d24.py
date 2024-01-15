import pandas as pd

df1= pd.DataFrame({
    "city":["mumbai","delhi","banglore"],
    "temperature":[32,45,30],
})

df2 = pd.DataFrame({
    "city":["delhi","mumbai","banglore"],
    "humidity":[65,68,75]
})

df = pd.merge(df1,df2,on='city')
print(df)
#        city  temperature  humidity
# 0    mumbai           32        68
# 1     delhi           45        65
# 2  banglore           30        75