import pandas as pd

# creating data frame by reading csv file using pandas
df = pd.read_csv("./Book1.csv")
print (df)
print(df.shape) #printing the dimesion[num of rows and columns]
rows,columns = df.shape #(6,4)
print(rows) #6
print(columns) #4

# creating data frame by using python dictionarie
weather_data = {
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature':[32,35,28,24,32,31],
    'windspeed':[6,7,2,7,4,2],
    'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df=pd.DataFrame(weather_data)
print(df)
