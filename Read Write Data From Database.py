import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost:3306/application")

df = pd.read_sql_table("customers",engine)
print(df)

df = pd.read_sql_table("customers",engine,columns=['name','phone_number'])
print(df)

query = "select customers.name, customers.phone_number,orders.name,orders.amount from customers join orders on customers.id = orders.customer_id"
df1 = pd.read_sql_query(query,engine)
print(df1)

