import pyodbc
import sqlalchemy
import psycopg2 as db

# Creating connection string

conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"

# Create connection object by passing the connection string into connect method

conn = db.connect(conn_string)

# Create cursor from connection

cur = conn.cursor()

# Create and execute query

query = 'select * from "People"'

cur.execute(query)

# print output row by row

for record in cur:
	print(record)

# Alternatives
# cur.fetchall()
# cur.fetchmany(howmany) ## how many is the number of records required
# cur.fetchone()

# to get row count
print("row count",cur.rowcount)

# To get the current row number cur.rownumber fetchone increments this by one

f = open('files/frompostgresdb.csv','w')

# use copy to to export cur to a file
f= open('files/frompostgresdb.csv','r')
f.read()

