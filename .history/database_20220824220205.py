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

#create a database
# my_cursor.execute("CREATE DATABASE files")
# my_cursor.execute("SHOW DATABASES")
my_cursor.execute("CREATE TABLE filename (name VARCHAR(255), uid INTEGER PRIMARY KEY)")


for db in my_cursor:
    print(db[0])
