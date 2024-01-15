import pandas as pd

df = pd.read_excel("stock_data.xlsx","stock_data")

# creating new excel file with the datas in df
df = df.to_excel("new.xlsx","stock")

# defining from which row and which column the data should be written in the excel file
df = df.to_excel("new.xlsx","stock",startrow=5,startcol=4)

# skip indexing
df = df.to_excel("new.xlsx","stock",index=False)
print(df)


