import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost:3306/application")

# reading a csv file
df = pd.read_csv("customers.csv")
# renaming the csv file's column title same as data base
df.rename(
    columns ={
        'Customer_name' : 'name',
        'phone_num' : 'phone_number'
},inplace=True)

# writing the csv file to database
df.to_sql('customers',engine,index=False,if_exists='append')

# read_sql() function
df = pd.read_sql("customers",engine)
print(df)

