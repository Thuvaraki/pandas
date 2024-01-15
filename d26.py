import pandas as pd

df = pd.read_csv("d25.csv")

new_df = df.pivot_table(index="city",columns="day")
print(new_df)
#            humidity            temperature
# day      05/01/2027 05/02/2017  05/01/2027 05/02/2017
# city
# mumbai         81.5       55.5        76.5       81.0
# new york       60.0       61.0        63.0       71.0

new_df = df.pivot_table(index="city",columns="day",aggfunc="sum")
print(new_df)
#            humidity            temperature
# day      05/01/2027 05/02/2017  05/01/2027 05/02/2017
# city
# mumbai        163.0      111.0       153.0      162.0
# new york      120.0      122.0       126.0      142.0