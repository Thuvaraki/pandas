import pandas as pd

# creating data frame by reading csv file using pandas
df = pd.read_csv("./Book1.csv")

# head() method gives the convenient to print only few rows
print(df.head(2)) #print only first 2 rows
print(df.head())  #print only first 5 rows

print(df.tail()) #print only last 5 rows
print(df.tail(3)) #print only laast 3 rows
