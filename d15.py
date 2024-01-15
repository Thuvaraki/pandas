import pandas as pd

df = pd.read_csv("Book1.csv")
# Filling NaN values with 0
new_df = df.fillna(0)

# filling NaN with different values in different columns
new_df = df.fillna({
    'temperature':0,
    'windspeed' : 0,
    'event': 'no event'
})

new_df = df.fillna(method="ffill") #forwardfill, copying forward values for NaN
new_df = df.fillna(method="ffill", limit=1) #copy the forwad value only for one cell
print(new_df)

new_df = df.fillna(method="bfill") #backwardfill, copying next values for NaN
print(new_df)

