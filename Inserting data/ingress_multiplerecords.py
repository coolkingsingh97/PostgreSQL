import pyodbc
import sqlalchemy
import psycopg2 as db
from faker import Faker

# Initialize faker object
fake = Faker()
# Initialize array to store all the data
data = []
# initializing i to hold an id
i=2

# iterate and append to data array
for r in range(1000):
	data.append((fake.name(),i,fake.street_address(),fake.city(),fake.zipcode()))
	i+=1
# convert array into tuple of tuples
data_for_db = tuple(data)

# Creating connection string

conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"

# Create connection object by passing the connection string into connect method

conn = db.connect(conn_string)

# Create cursor from connection

cur = conn.cursor()

# NOTE: table name is case sensitive and needs to be in double quotes
query = 'insert into "People" (name,id,street,city,zip) values (%s,%s,%s,%s,%s)'

# print out what code will be sent to DB
print(cur.mogrify(query,data_for_db[1]))

# using EXECUTEMANY to let the library handle multiple inserts
cur.executemany(query,data_for_db)
conn.commit()

