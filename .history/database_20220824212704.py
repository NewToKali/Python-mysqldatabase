import mysql.connector 
mydb= mysql.connector.connect (
    host= "127.0.01",
    user="root",
    passwd="admin"
)
print (mydb)