import mysql.connector
import pandas as pd
import sqlalchemy as sqla

# cfg = open("config.json")

# read = cfg.read()

cnx = mysql.connector.connect(user="root", password="", host="localhost", database="classicmodels")

if cnx.is_connected():
    print('Connected Successfully')
else: 
    print('Connection Not Successful')

cursor = cnx.cursor()

query_statement = open("simple_query.sql")

query = query_statement.read()

# cursor.execute("SHOW DATABASES")

cursor.execute(query)

result = cursor.fetchall()

print(result)

cnx.close()

if cnx.is_closed():
        print('Closed Successfully')
else: 
    print('Connection Not Closed Successfully')

