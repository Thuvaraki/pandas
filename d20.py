import pandas as pd

india_weather= pd.DataFrame({
    "city":["mumbai","delhi","banglore"],
    "temperature":[32,45,30],
    "humidity" : [80,60,78]
})

us_weather = pd.DataFrame({
    "city":["new york","chicago","orlando"],
    "temperature":[21,14,35],
    "humidity" : [68,65,75]
})

df = pd.concat([india_weather,us_weather]) #here the index will be same as individual data frames
print(df)
#        city  temperature  humidity
# 0    mumbai           32        80
# 1     delhi           45        60
# 2  banglore           30        78
# 0  new york           21        68
# 1   chicago           14        65
# 2   orlando           35        75

df = pd.concat([india_weather,us_weather],ignore_index=True) #here the index will be same as individual data frames
print(df)
#        city  temperature  humidity
# 0    mumbai           32        80
# 1     delhi           45        60
# 2  banglore           30        78
# 3  new york           21        68
# 4   chicago           14        65
# 5   orlando           35        75

print("####################")
df = pd.concat([india_weather,us_weather],keys=["india","us"])
print(df)
#              city  temperature  humidity
# india 0    mumbai           32        80
#       1     delhi           45        60
#       2  banglore           30        78
# us    0  new york           21        68
#       1   chicago           14        65
#       2   orlando           35        75
print(df.loc["india"])
#        city  temperature  humidity
# 0    mumbai           32        80
# 1     delhi           45        60
# 2  banglore           30        78
print(df.loc["us"])
#        city  temperature  humidity
# 0  new york           21        68
# 1   chicago           14        65
# 2   orlando           35        75