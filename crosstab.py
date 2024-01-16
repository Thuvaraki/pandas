import pandas as pd
import numpy as np

df = pd.read_excel("survey.xls","New Text Document")
print(df)

x = pd.crosstab(df.Nationality,df.Handedness)
print(x)

x = pd.crosstab(df.Sex,df.Handedness)
print(x)

# Using margins
x = pd.crosstab(df.Sex,df.Handedness,margins=True)
print(x)

# using multiple columns
y = pd.crosstab(df.Sex,[df.Handedness,df.Nationality])
print(y)

# using multiple indexing
y = pd.crosstab([df.Nationality,df.Sex],df.Handedness)
print(y)

# normalize='index' is used to normalize the values along the index (rows), which means that each row will represent the proportions of each 'Handedness' category for a given 'Sex' category.
x = pd.crosstab(df.Sex,df. Handedness,normalize='index')
print(x)

x = pd.crosstab(df.Sex,df.Handedness,values=df.Age,aggfunc=np.average)
print(x)