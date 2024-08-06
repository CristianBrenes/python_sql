# importing dependencies 
import pymysql as pms
import pandas as pd
# from connections import databases

# connecting to the database
# cnx = mysql.connector.connect("connections/databases" + {classicmodels})
cnx = pms.connect(user="root", password="", host="localhost", database="classicmodels")

# if/else statement providing a print display whether the database connection is successful or unsuccessful
if cnx.Error():
    print('\n-Connection to the Database Successful-\n')
else: 
    print('\n-Connection to the Database Not Successful-\n')

# declaring cursor which enables you to specify the cell you want
cursor = cnx.cursor()

# specifying the SQL query file that you want to run
query_statement_open = open("sql_query_statement/" + input("Please enter the SQL file name: "))

# placing the data within the file into a variable
query = query_statement_open.read()

# executing the query using cursor.execute() which uses cursor to select the cells using the query
cursor.execute(query)

# fetching the results from the query execution
result = cursor.fetchall()

# creating a dataframe with the pulled data using pandas 
df = pd.DataFrame(result)

# printing the results of the query 
print(df)

# closing the connection to the database 
cnx.close()

# if/else statement reflecting if the disconnection is successful or unsuccessful 
if cnx.open:
        print('\n-Connection to the Database Not Closed Successfully-')
else: 
    print('\n-Connection to the Database Closed Successfully-')



