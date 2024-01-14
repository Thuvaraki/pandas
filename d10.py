import pandas as pd

df = pd.read_csv("stock_data.csv")

df.to_csv('new.csv') #will create a new csv file which is named as new in our directory

df.to_csv('new.csv',index=False) #removing the indexing

# exporting only tickers and eps columns to the new csv file
df.to_csv('new.csv',columns=['tickers','eps'])

# If we don't want to export the header to our new.csv file then header=False
df.to_csv('new.csv',header=False)
print(df)
