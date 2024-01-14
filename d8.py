import pandas as pd

# various types of creating data frame

#1
df = pd.read_csv("Book1.csv")

#2
df = pd.read_excel("Book1.xlsx","Sheet1")

#3
weather_data = {
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature':[32,35,28,24,32,31],
    'windspeed':[6,7,2,7,4,2],
    'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df=pd.DataFrame(weather_data)

#4
df=pd.DataFrame(weather_data , columns=["day","windspeed","event","temperature"])

#5
weather_data = [
    {'day':'1/1/2017','temperature':'32','windspeed':'6','event':'Rain'},
    {'day':'1/2/2017','temperature':'35','windspeed':'7','event':'Sunny'},
    {'day':'1/3/2017','temperature':'28','windspeed':'2','event':'Snow'}
]
df=pd.DataFrame(weather_data)
print(df)