import pandas as pd

df = pd.read_csv("./Book1.csv")
print(df) #print entire dataframe
print(df[:]) #print entire dataframe

print(df[2:5]) #print from row num 2 to 4(5 exclusive) in  dataframe

print(df.columns) #print the columns

print(df.day) #printing the content in the day column
#printing the content in the event column
print(df.event)
print(df['event'])