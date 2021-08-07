import psycopg2 as db
import pandas as pd

# Setting up the connection
conn_string= "dbname='dataengineering' host = 'localhost' user='postgres' password='postgres'"
conn =db.connect(conn_string)
# Extract query into pandas dataframe
df =pd.read_sql('select * from "People"',conn)
# Extract dataframe into JSON
df.to_json('C:/Users/Kulraj/Documents/GitHub/PostgreSQL/extracting data/files/frompostgres.json',orient='records')

