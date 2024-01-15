import pandas as pd

df1= pd.DataFrame({
    "city":["mumbai","delhi","banglore","kolkatta"],
    "temperature":[32,45,30,50],
})

df2 = pd.DataFrame({
    "city":["delhi","mumbai","tamilnaadu"],
    "humidity":[65,68,75]
})

print("##### inner join ##### ")
df = pd.merge(df1,df2,on='city')
print(df)
#      city  temperature  humidity
# 0  mumbai           32        68
# 1   delhi           45        65

print("##### outer join ##### ")
df = pd.merge(df1,df2,how="outer")
print(df)
#          city  temperature  humidity
# 0      mumbai         32.0      68.0
# 1       delhi         45.0      65.0
# 2    banglore         30.0       NaN
# 3    kolkatta         50.0       NaN

print("##### left join ##### ")
df = pd.merge(df1,df2,how="left")
print(df)
#        city  temperature  humidity
# 0    mumbai           32      68.0
# 1     delhi           45      65.0
# 2  banglore           30       NaN
# 3  kolkatta           50       NaN

print("##### right join ##### ")
df = pd.merge(df1,df2,how="right")
print(df)
#         city  temperature  humidity
# 0       delhi         45.0        65
# 1      mumbai         32.0        68
# 2  tamilnaadu          NaN        75

print("##### Suffixes #####")
Df1= pd.DataFrame({
    "city":["mumbai","delhi","banglore","kolkatta"],
    "temperature":[32,45,30,50],
})

Df2 = pd.DataFrame({
    "city":["delhi","mumbai"],
    "temperature":[65,68]
})

df= pd.merge(Df1,Df2,on='city')
print(df)
#      city  temperature_x  temperature_y
# 0  mumbai             32             68
# 1   delhi             45             65

# defining suffix
df= pd.merge(Df1,Df2,on='city',suffixes=('_left','_right'))
print(df)
#      city  temperature_left  temperature_right
# 0  mumbai                32                 68
# 1   delhi                45                 65
