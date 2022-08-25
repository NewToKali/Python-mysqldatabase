# pip install mysql-connector-python
import mysql.connector
mydb= mysql.connector.connect (
    host= "127.0.0.1",
    user="root",
    passwd="admin",
    database="files"
)
# print (mydb)
#Create a cursor 
my_cursor= mydb.cursor()

#create a database 'once you create a database add the "database" to mydb'
# my_cursor.execute("CREATE DATABASE files")
# my_cursor.execute("SHOW DATABASES")
# add a table to database
# my_cursor.execute("CREATE TABLE filename (name VARCHAR(255), uid INTEGER PRIMARY KEY)")
# my_cursor.execute("SHOW TABLES")
#add files to database
testfile="ewbfile"
testuid=354

sql_insert="INSERT INTO files (name, uid) VALUES (%s,%s) "
record1= (testfile, testuid)
mydb.commit()
# for db in my_cursor:
#     print(db[0])
