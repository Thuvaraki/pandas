import pandas as pd

# Creating a Period object for the year 2023
x = pd.Period('2023')
print(x)
# 2023

# Printing the attributes and methods of the Period object
print(dir(x))

# Accessing the start time of the period
print(x.start_time)
# 2023-01-01 00:00:00

# Accessing the end time of the period
print(x.end_time)
# 2023-12-31 23:59:59.999999999

#####################Monthly Period############################
m = pd.Period('2023-10',freq='M')
print(m)
# 2023-10

print(m.start_time) #2023-10-01 00:00:00
print(m.end_time) #2023-10-31 23:59:59.999999999
print(m+1) #2023-11

######################Daily Period###########################
d = pd.Period('2023-10-12',freq='D')
print(d) #2023-10-12

print(d.start_time) #2023-10-12 00:00:00
print(d.end_time) #2023-10-12 23:59:59.999999999
print(d+1) #2023-10-13
print(d+pd.offsets.Day(3)) #2023-10-15

#######################Quartely time period####################
q = pd.Period('2023Q1')
print(q)
print(q+1)

q1= pd.Period('2023Q1', freq='Q-JAN') #specifyig the year end is January
print(q1)
print(q1.start_time) #2022-02-01 00:00:00
print(q1.end_time) #2022-04-30 23:59:59.999999999

# Use asfreq to convert period to a different frequency
print(q1.asfreq('M',how='start')) #2022-02
print(q1.asfreq('M',how='end')) #2022-04
