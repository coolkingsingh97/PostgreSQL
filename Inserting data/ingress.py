import pyodbc
import sqlalchemy
import psycopg2 as db

# Creating connection string

conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"

# Create connection object by passing the connection string into connect method

conn = db.connect(conn_string)

# Create cursor from connection

cur = conn.cursor()

# Create SQL query to insert data

query = "insert into people (id, name, street, city, zip) values({},'{}','{}','{}','{}')".format(1,'Big Bird','Sesame Street','Fakeville','12345')

# Use mogrify method to see what you will be sending to the database

cur.mogrify(query)

# NOTE: table name is case sensitive and needs to be in double quotes
query2 = 'insert into "People" (name,id,street,city,zip) values (%s,%s,%s,%s,%s)'
data = ('Big Bird',1,'Sesame Street','Fakeville','12345')

cur.mogrify(query2,data)

# Execute query to add to the database

cur.execute(query2,data)

# Query is not permanent unless you can commit it
conn.commit()