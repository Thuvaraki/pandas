import pandas as pd

df = pd.read_csv("d25.csv")

new_df = df.pivot_table(index="city",columns="day",aggfunc="mean")
print(new_df)

new_df = df.pivot_table(index="city",columns="day",aggfunc="diff")
print(new_df)

new_df = df.pivot_table(index="city",columns="day",aggfunc="count")
print(new_df)

new_df = df.pivot_table(index="city",columns="day",margins=True)
print(new_df)
#            humidity                  temperature
# day      05/01/2027 05/02/2017   All  05/01/2027 05/02/2017     All
# city
# mumbai        81.50      55.50  68.5       76.50       81.0  78.750
# new york      60.00      61.00  60.5       63.00       71.0  67.000
# All           70.75      58.25  64.5       69.75       76.0  72.875