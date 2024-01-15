import pandas as pd
import numpy as np

df = pd.read_csv("d18.csv")

# replace -99999 with NaN
new_df = df.replace(-99999,np.NaN)

# replace -99999 and -88888 with NaN
new_df = df.replace([-88888,-99999],np.NaN)

# #######
new_df = df.replace({
    'temperature':-99999,
    'windspeed':-99999,
    'event':'0'
},np.NaN)

############
new_df = df.replace({
    -99999:np.NaN,
    'No Event':'Sunny'
})
print(new_df)