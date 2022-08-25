import mysql.connector as mysql
mydb= mysql.connect (
    host= "127.0.0.1",
    user="root",
    passwd="admin"
)
print (mydb)