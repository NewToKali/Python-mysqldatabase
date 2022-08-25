# pip install mysql-connector-python
import mysql.connector
mydb= mysql.connector.connect (
    host= "127.0.0.1",
    user="root",
    passwd="admin"
)
# print (mydb)
#Create a cursor 
my_cursor= mydb.cursor()
m