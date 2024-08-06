# connects to the database using credentials
__connection_variable__ = mysql.connector.connect(user="", password="", host="", database="")

# is used to check is you are connected to the database. usually used in a print statement to display connection succesful
__connection_variable__.is_connected()

# cursor is a "object" that is used to pinpoint information cell by cell like a selector
__cursor_variable__ = __connection_variable__.cursor()

# this is the command that pulls that data from the .execute() command above and placing it in a variable
__result_variable__ = __cursor_variable__.fetchall()

# this is used to close the connection to the database. could be used with a print to ensure disconnection
__connection_variable__.close()

# example on how to CREATE a DB
__database_name_create_variable__ = """CREATE TABLE `__database_name__`.`__desired_table_name__` (
  `__column_name__` __data_type__ __null_allow_or_not__ __auto_increment__,
  `__column_name__` __data_type__ __null_allow_or_not__,
  `__column_name__` __data_type__ __null_allow_or_not__,
  `__column_name__` __data_type__ __null_allow_or_not__,
   PRIMARY KEY (`__desired_column_for_primary_key__`))"""

# example on how to INSERT data into a DB
# insert statement for tblemployee
# this statement will enable us to insert multiple rows at once.
__database_name_insert_variable__ = """INSERT INTO __database_name__ (
   __column_name__,
   __column_name__,
   __column_name__) 
   VALUES  (%s, %s, %s)""" # unsure of the sytax in this line. if $ is needed and if the "s" means string
 
# we save all the row data to be inserted in a data variable
__data_variable__ = [("__first_column_data__", "__second_column_data__", "__third_column_data__"),
        ("__first_column_data__", "__second_column_data__", "__third_column_data__"),
        ("__first_column_data__", "__second_column_data__", "__third_column_data__"),
        ("__first_column_data__", "__second_column_data__", "__third_column_data__")]
 
# execute the insert commands for all rows and commit to the database
c.executemany(__database_name_insert_variable__, __data_variable__)

# update statement for tblemployee
# which modifies the salary of Vani
# back slash is a "enter" next line
__database_name_update_variable__ = "UPDATE __database_name\
SET __column_name__ = __desired_update__ WHERE __colum_name__ = __column_data__"

# deleting query
__database_name_update_variable__ = "DELETE FROM __database_name__ WHERE __column_name__ = __column_data__"
cursorObject.execute(__database_name_update_variable__, __values_being_deleted__)

# commits the changes to the DB
db.commit()

# is used to run the SQL query within the parenthesis. Could be a variable holding the query as well.
__query_variable__.execute()

