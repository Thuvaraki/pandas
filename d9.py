import pandas as pd

# skiprows=1 -> Here the first line will be skipped
df = pd.read_csv("stock_data.csv",skiprows=1)

# Here it says that my header located at the row number 1 and that line will be skipped
df = pd.read_csv("stock_data.csv",header=1)

# if we missed header in pur csv file then we can specify header like below
df = pd.read_csv("stock_data.csv",header=None,names=["ticker","eps","revenue","price","people"])
print(df)

# to retrieve first 3 rows excluding the header from the csv file
df = pd.read_csv("stock_data.csv",nrows=3)

# replacing the not available or n.a. values with NaN
df = pd.read_csv("stock_data.csv",na_values=["not available", "n.a."])

# revenue can not be negative but we can't directly use the above method bcz the -1 in eps
# also will be replaced. So we are using dictionaries
df = pd.read_csv("stock_data.csv",na_values={
    'eps' : ["not available", "n.a."],
    'revenue' : ["not available", "n.a.",-1],
    'people' : ["not available", "n.a."]
})
print(df)