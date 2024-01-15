import pandas as pd

df = pd.read_csv("d28.csv")
print(df)
#          day  Chicago  Chennai  Berlin
# 0     Monday       32       75      41
# 1    Tuesday       30       77      43
# 2  Wednesday       28       75      45
# 3   Thursday       22       82      38
# 4     Friday       30       83      30
# 5   Saturday       20       81      45
# 6     Sunday       25       77      47

# id_vars parameter specifies the columns that you want to keep as identifiers (unchanged) in the melted DataFrame
df1 = pd.melt(df,id_vars= ["day"])
print(df1)
#          day variable  value
# 0      Monday  Chicago     32
# 1     Tuesday  Chicago     30
# 2   Wednesday  Chicago     28
# 3    Thursday  Chicago     22
# 4      Friday  Chicago     30
# 5    Saturday  Chicago     20
# 6      Sunday  Chicago     25
# 7      Monday  Chennai     75
# 8     Tuesday  Chennai     77
# 9   Wednesday  Chennai     75
# 10   Thursday  Chennai     82
# 11     Friday  Chennai     83
# 12   Saturday  Chennai     81
# 13     Sunday  Chennai     77
# 14     Monday   Berlin     41
# 15    Tuesday   Berlin     43
# 16  Wednesday   Berlin     45
# 17   Thursday   Berlin     38
# 18     Friday   Berlin     30
# 19   Saturday   Berlin     45
# 20     Sunday   Berlin     47

new_df = df1[df1["variable"]=="Chicago"]
print(new_df)
#          day variable  value
# 0     Monday  Chicago     32
# 1    Tuesday  Chicago     30
# 2  Wednesday  Chicago     28
# 3   Thursday  Chicago     22
# 4     Friday  Chicago     30
# 5   Saturday  Chicago     20
# 6     Sunday  Chicago     25

df2 = pd.melt(df,id_vars= ["day"],var_name="City",value_name="Temperature")
print(df2)
#           day     City  Temperature
# 0      Monday  Chicago           32
# 1     Tuesday  Chicago           30
# 2   Wednesday  Chicago           28
# 3    Thursday  Chicago           22
# 4      Friday  Chicago           30
# 5    Saturday  Chicago           20
# 6      Sunday  Chicago           25
# 7      Monday  Chennai           75
# 8     Tuesday  Chennai           77
# 9   Wednesday  Chennai           75
# 10   Thursday  Chennai           82
# 11     Friday  Chennai           83
# 12   Saturday  Chennai           81
# 13     Sunday  Chennai           77
# 14     Monday   Berlin           41
# 15    Tuesday   Berlin           43
# 16  Wednesday   Berlin           45
# 17   Thursday   Berlin           38
# 18     Friday   Berlin           30
# 19   Saturday   Berlin           45
# 20     Sunday   Berlin           47

