import pandas as pd

df = pd.read_csv("democsv.csv")
print(df)

#  Unnamed: 0  temperature  windspeed   event
# 0         day          NaN        NaN     NaN
# 1  01/01/2017         32.0        6.0    Rain
# 2  04/01/2017          NaN        9.0   Sunny
# 3  05/01/2017         28.0        9.0    Snow
# 4  06/01/2017         28.0        7.0    Snow
# 5  07/01/2017         32.0        7.0    Rain
# 6  08/01/2017         32.0        7.0   Sunny
# 7  09/01/2017         32.0        NaN   Sunny
# 8  10/01/2017         34.0        8.0  Cloudy
# 9  11/01/2017         40.0       12.0   Sunny

# interpolate() function in pandas is used to fill missing values in a DataFrame
new_df= df.interpolate()
print(new_df)
#    Unnamed: 0  temperature  windspeed   event
# 0         day          NaN        NaN     NaN
# 1  01/01/2017         32.0        6.0    Rain
# 2  04/01/2017         30.0        9.0   Sunny
# 3  05/01/2017         28.0        9.0    Snow
# 4  06/01/2017         28.0        7.0    Snow
# 5  07/01/2017         32.0        7.0    Rain
# 6  08/01/2017         32.0        7.0   Sunny
# 7  09/01/2017         32.0        7.5   Sunny
# 8  10/01/2017         34.0        8.0  Cloudy
# 9  11/01/2017         40.0       12.0   Sunny

new_df= df.interpolate(method='time')
print(new_df)
##    Unnamed: 0  temperature  windspeed   event
# 0         day          NaN        NaN     NaN
# 1  01/01/2017         32.0        6.0    Rain
# 2  04/01/2017         29.0        9.0   Sunny
# 3  05/01/2017         28.0        9.0    Snow
# 4  06/01/2017         28.0        7.0    Snow
# 5  07/01/2017         32.0        7.0    Rain
# 6  08/01/2017         32.0        7.0   Sunny
# 7  09/01/2017         32.0        7.5   Sunny
# 8  10/01/2017         34.0        8.0  Cloudy
# 9  11/01/2017         40.0       12.0   Sunny