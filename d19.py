import pandas as pd

df=pd.read_csv("d19.csv")
print(df)

g = df.groupby('city') #here g is the dataframe group by object
for city,city_df in g:
    print(city)
    print(city_df)

#finding maximum temperature of each city
print(g.max())
print(g.min())
# print(g.mean())
print(g.describe())
print(g.plot())
