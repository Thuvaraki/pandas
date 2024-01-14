import pandas as pd

df = pd.read_csv("./Book1.csv")

# printing the entire row where the temperature is >=35
print(df[df.temperature>=35])

# print entire row where temperature is max
print(df[df.temperature == df.temperature.max()])

