# pip install mysql-connector-python
import mysql.connector
mydb= mysql.connector.connect (
    host= "127.0.0.1",
    user="root",
    passwd="admin",
    datb
)
# print (mydb)
#Create a cursor 
my_cursor= mydb.cursor()
#create a table
# my_cursor.execute("CREATE DATABASE files")
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db[0])
